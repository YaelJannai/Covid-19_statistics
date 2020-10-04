import json

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

# the url to scrape
URL = "https://disease.sh/v3/covid-19/historical/{country}?lastdays=31"


def findCountry():
    """
    Find the country from the user input url.
    :return: the country name
    """
    # get the country from the user input
    country = request.args.get("country")
    # in case the country is written in upper case
    country = country.lower()
    return country


def getPeaks(country):
    """
    Get the data from the url, using requests library.
    :param country: the country the user wrote, to search data for that specific country.
    :return: the entire data structure fetched.
    """
    # use the country from the user input
    search_url = URL.replace('{country}', country)
    # access that url
    all_peaks = requests.get(search_url)
    return all_peaks


def getMax(cases_dict):
    """
    Create a new dictionary of differance values, return the maximum value.
    :param cases_dict: The dictionary of cases/ deaths/ recovered.
    :return: Returns the date and value of the highest peak from dictionary.
    """
    # get values from dictionary
    val_dict = list(cases_dict.values())
    # get keys from dictionary
    key_list = list(cases_dict.keys())
    count = 1
    # new dictionary for the differance
    diff_dict = {}
    # calculate difference because it is originally held as accumulated value
    for val1, val2 in zip(val_dict[0::], val_dict[1::]):
        # calculate differance between each 2 adjacent values
        diff_dict[key_list[count]] = val2 - val1
        count += 1
    # get the maximum differance - this is the peak
    max_val = max(diff_dict, key=diff_dict.get)
    return max_val, diff_dict[max_val]


class NewCasesPeak(Resource):
    def get(self):
        country = findCountry()
        peaks = getPeaks(country)
        if peaks.status_code == 404:
            return {}
        else:
            new_cases = json.loads(peaks.text)["timeline"]["cases"]
            date, value = getMax(new_cases)
            return {"country": country, "method": self.__class__.__name__, "date": date, "value": value}


class RecoveredPeak(Resource):
    def get(self):
        country = findCountry()
        peaks = getPeaks(country)
        if peaks.status_code == 404:
            return {}
        else:
            recovered = json.loads(peaks.text)["timeline"]["recovered"]
            date, value = getMax(recovered)
        return {"country": country, "method": self.__class__.__name__, "date": date, "value": value}


class DeathsPeak(Resource):
    def get(self):
        country = findCountry()
        peaks = getPeaks(country)
        if peaks.status_code == 404:
            return {}
        else:
            deaths = json.loads(peaks.text)["timeline"]["deaths"]
            date, value = getMax(deaths)
        return jsonify({"country": country, "method": self.__class__.__name__, "date": date, "value": value})


class Status(Resource):
    """
    Method to return a value of success / fail to contact the backend API.
    """
    @staticmethod
    def get():
        # connect to that -->
        check_api = "https://disease.sh/v3/covid-19/jhucsse"
        ret_status = requests.get(check_api).status_code
        # success
        if ret_status == 200:
            return {'status': "success"}
        # fail
        return {'status': "fail"}


class HandleErrors(Resource):
    """
    In order to support error handling.
    """
    @staticmethod
    def get(path=''):
        # get default empty path, return {}
        return {}


# add the routes to the api
api.add_resource(NewCasesPeak, '/newCasesPeak')
api.add_resource(RecoveredPeak, '/recoveredPeak')
api.add_resource(DeathsPeak, '/deathsPeak')
api.add_resource(Status, '/status')
api.add_resource(HandleErrors, '/<path:path>', '/')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
