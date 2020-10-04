# Covid-19_statistics

This script job is to fetch Covid-19 data from https://corona.lmao.ninja API.
It contains a Python service that scrapes data from external API.

The service's job:
* Response with JSON format on any request (support error handling).
* Scrape data from an external API to retrieve Covid-19 data.
* Serve 4 endpoints:
    ○ newCasesPeak - Returns the date (and value) of the highest peak of new Covid-19 cases in the last 30 days for a required country.
    ○ recoveredPeak - Returns the date (and value) of the highest peak of recovered Covid-19 cases in the last 30 days for the required country.
    ○ deathsPeak - Returns the date (and value) of the highest peak of death Covid-19 cases in the last 30 days for a required country.
    ○ status - Returns a value of success / fail to contact the backend API.


Examples:
1.    curl localhost:8080/status
      {“status”: “success”}
    
2.    curl localhost:8080/deathsPeak?country=spain
      {"country": "spain", "method": "RecoveredPeak", "date": "9/30/20", "value": 380}
