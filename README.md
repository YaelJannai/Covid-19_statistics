# Covid-19_statistics

## Python Script:
This script job is to fetch Covid-19 data from https://corona.lmao.ninja API.  
It contains a Python service that scrapes data from external API.

The service's job:
* Response with JSON format on any request (support error handling).
* Scrape data from an external API to retrieve Covid-19 data.
* Serve 4 endpoints:		
	* newCasesPeak - Returns the date (and value) of the highest peak of new Covid-19 cases in the last 30 days for a required country.		
	* recoveredPeak - Returns the date (and value) of the highest peak of recovered Covid-19 cases in the last 30 days for the required country.		
	* deathsPeak - Returns the date (and value) of the highest peak of death Covid-19 cases in the last 30 days for a required country.		
	* status - Returns a value of success / fail to contact the backend API.

Examples for python script:
* **request**:     curl localhost:5000/status
	* **response**: 	  {“status”: “success”}
    
* **request**:     curl localhost:5000/deathsPeak?country=spain
	* **response**:	  {"country": "spain", "method": "RecoveredPeak", "date": "9/30/20", "value": 380}
   
<br/><br/>   
   
## Jenkins Job:
What this job does:
1. Clone this git repository
2. Start the Python service
3. Query the python service with several country values. The request to the service & results for each of the queries will be shown on the job console view in jenkins.

The job gets as input parameters a list of queries separated by comma, and then it executes each query separately one-by-one.  
The query and its result are printed to the job's console.

The input is inserted in the following way - 
![GitHub Logo](https://github.com/YaelJannai/Covid-19_statistics/blob/main/input.png)
