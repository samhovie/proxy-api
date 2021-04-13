import flask
import requests
import json
import time
import os
from flask import Flask, render_template, url_for, json, send_from_directory
from pathlib import Path


# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

USERS = [
	{
		"username": "awdeorio",
		"snippets": []
	},
	{
		"username": "shahamy",
		"snippets": []
	},
]
# main page
@app.route("/", methods=["GET"])
def get_index():
	context = {
		"text": "THIS IS THE MAIN INDEX.HTML"
	}
	return flask.jsonify(**context)

# returns list of API end points
@app.route("/api/CDT/<county>", methods=["GET"])
def get_cdt(county):
    SITE_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
    json_url = os.path.join(SITE_ROOT, 'CDT', county + '.json')
    data = json.load(open(json_url))
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/api/VACCINE/<county>", methods=["GET"])
def get_vaccine(county):
    SITE_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
    json_url = os.path.join(SITE_ROOT, 'VACCINE', county + '.json')
    data = json.load(open(json_url))
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/api/TESTS/<county>", methods=["GET"])
def get_tests(county):
    SITE_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
    json_url = os.path.join(SITE_ROOT, 'TESTS', county + '.json')
    data = json.load(open(json_url))
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/api/CLI/", methods=["GET"])
def get_cli():
    SITE_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
    json_url = os.path.join(SITE_ROOT, 'CLI', 'GetResurgenceDataCLIAdmissions.json')
    data = json.load(open(json_url))
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

# returns list of users
@app.route("/api/v1/users/", methods=["GET"])
def get_users_list():
	context = {
		"count": len(USERS),
		"results": USERS
	}
	return flask.jsonify(**context)

if __name__ == "__main__":
	app.run(host="localhost", port=8000, debug=True)


@app.cli.command()
def scheduled():
    """Run scheduled job."""
    countyMap = {
      "ADAMS": {
         "covid_region": 3
      },
      "ALEXANDER": {
         "covid_region": 5
      },
      "BOND": {
         "covid_region": 4
      },
      "BOONE": {
         "covid_region": 1
      },
      "BROWN": {
         "covid_region": 3
      },
      "BUREAU": {
         "covid_region": 2
      },                   
      "CALHOUN": {
         "covid_region": 3
      },
      "CARROLL": {
         "covid_region": 1
      },
      "CASS": {
         "covid_region": 3
      },
      "CHAMPAIGN": {
         "covid_region": 6
      },
      "CHICAGO": {
         "covid_region": 11
      },
      "CHRISTIAN": {
         "covid_region": 3
      },
      "CLARK": {
         "covid_region": 6
      },
      "CLAY": {
         "covid_region": 6
      },
      "CLINTON": {
         "covid_region": 4
      },
      "COLES": {
         "covid_region": 6
      },
      "COOK": {
         "covid_region": 10
      },
      "CRAWFORD": {
         "covid_region": 6
      },
      "CUMBERLAND": {
         "covid_region": 6
      },
      "DE WITT": {
         "covid_region": 6
      },
      "DEKALB": {
         "covid_region": 1
      },
      "DOUGLAS": {
         "covid_region": 6
      },
      "DUPAGE": {
         "covid_region": 8
      },
      "EDGAR": {
         "covid_region": 6
      },
      "EDWARDS": {
         "covid_region": 5
      },
      "EFFINGHAM": {
         "covid_region": 6
      },
      "FAYETTE": {
         "covid_region": 6
      },
      "FORD": {
         "covid_region": 6
      },
      "FRANKLIN": {
         "covid_region": 5
      },
      "FULTON": {
         "covid_region": 2
      },
      "GALLATIN": {
         "covid_region": 5
      },
      "GREENE": {
         "covid_region": 3
      },
      "GRUNDY": {
         "covid_region": 2
      },
      "HAMILTON": {
         "covid_region": 5
      },
      "HANCOCK": {
         "covid_region": 3
      },
      "HARDIN": {
         "covid_region": 5
      },
      "HENDERSON": {
         "covid_region": 2
      },
      "HENRY": {
         "covid_region": 2
      },
      "IROQUOIS": {
         "covid_region": 6
      },
      "JACKSON": {
         "covid_region": 5
      },
      "JASPER": {
         "covid_region": 6
      },
      "JEFFERSON": {
         "covid_region": 5
      },
      "JERSEY": {
         "covid_region": 3
      },
      "JO DAVIESS": {
         "covid_region": 1
      },
      "JOHNSON": {
         "covid_region": 5
      },
      "KANE": {
         "covid_region": 8
      },
      "KANKAKEE": {
         "covid_region": 7
      },
      "KENDALL": {
         "covid_region": 2
      },
      "KNOX": {
         "covid_region": 2
      },
      "LAKE": {
         "covid_region": 9
      },
      "LASALLE": {
         "covid_region": 2
      },
      "LAWRENCE": {
         "covid_region": 6
      },
      "LEE": {
         "covid_region": 1
      },
      "LIVINGSTON": {
         "covid_region": 2
      },
      "LOGAN": {
         "covid_region": 3
      },
      "MACON": {
         "covid_region": 6
      },
      "MACOUPIN": {
         "covid_region": 3
      },
      "MADISON": {
         "covid_region": 4
      },
      "MARION": {
         "covid_region": 5
      },
      "MARSHALL": {
         "covid_region": 2
      },
      "MASON": {
         "covid_region": 3
      },
      "MASSAC": {
         "covid_region": 5
      },
      "MCDONOUGH": {
         "covid_region": 2
      },
      "MCHENRY": {
         "covid_region": 9
      },
      "MCLEAN": {
         "covid_region": 2
      },
      "MENARD": {
         "covid_region": 3
      },
      "MERCER": {
         "covid_region": 2
      },
      "MONROE": {
         "covid_region": 4
      },
      "MONTGOMERY": {
         "covid_region": 3
      },
      "MORGAN": {
         "covid_region": 3
      },
      "MOULTRIE": {
         "covid_region": 6
      },
      "OGLE": {
         "covid_region": 1
      },
      "PEORIA": {
         "covid_region": 2
      },
      "PERRY": {
         "covid_region": 5
      },
      "PIATT": {
         "covid_region": 6
      },
      "PIKE": {
         "covid_region": 3
      },
      "POPE": {
         "covid_region": 5
      },
      "PULASKI": {
         "covid_region": 5
      },
      "PUTNAM": {
         "covid_region": 2
      },
      "RANDOLPH": {
         "covid_region": 4
      },
      "RICHLAND": {
         "covid_region": 6
      },
      "ROCK ISLAND": {
         "covid_region": 2
      },
      "SALINE": {
         "covid_region": 5
      },
      "SANGAMON": {
         "covid_region": 3
      },
      "SCHUYLER": {
         "covid_region": 3 
      },
      "SCOTT": {
         "covid_region": 3
      },
      "SHELBY": {
         "covid_region": 6
      },
      "ST. CLAIR": {
         "covid_region": 4
      },
      "STARK": {
         "covid_region": 2
      },
      "STEPHENSON": {
         "covid_region": 1
      },
      "TAZEWELL": {
         "covid_region": 2
      },
      "UNION": {
         "covid_region": 5
      },
      "VERMILION": {
         "covid_region": 6
      },
      "WABASH": {
         "covid_region": 5
      },
      "WARREN": {
         "covid_region": 2
      },
      "WASHINGTON": {
         "covid_region": 4
      },
      "WAYNE": {
         "covid_region": 5
      },
      "WHITE": {
         "covid_region": 5
      },
      "WHITESIDE": {
         "covid_region": 1
      },
      "WILL": {
         "covid_region": 7
      },
      "WILLIAMSON": {
         "covid_region": 5
      },
      "WINNEBAGO": {
         "covid_region": 1
      },
      "WOODFORD": {
         "covid_region": 2
      },
      "ILLINOIS": {
         "covid_region": 0
      }
    }
    cdt_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVID/GetCountyHistorical?countyName='
    test_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVID/GetCountyHistorical?countyName='
    vacc_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVIDVaccine/getVaccineAdministration?CountyName='
    
    cli_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVIDExport/GetResurgenceDataCLIAdmissions'
    cdt_urls = []
    test_urls = []
    vacc_urls = []
    CDT = []
    TESTS = []
    VACCINE = []
    
    for county in countyMap:
       cdt_urls.append(cdt_url + county)
       test_urls.append(test_url + county)
       vacc_urls.append(vacc_url + county)
    
    for url in cdt_urls:
        r = requests.get(url)
        json_data = json.loads(r.text)
        county = url.split('=')[-1]
        for entry in json_data['values']:
            CDT.append(entry)
    
    base = Path()
    jsonpath = base / ("CDT.json")
    # base.mkdir(exist_ok=True)
    jsonpath.write_text(json.dumps(CDT, indent=4))

    for url in test_urls:
        r = requests.get(url)
        json_data = json.loads(r.text)
        county = url.split('=')[-1]
        for entry in json_data['values']:
            TESTS.append(entry)
    
    base = Path()
    jsonpath = base / ("TESTS.json")
    # base.mkdir(exist_ok=True)
    jsonpath.write_text(json.dumps(TESTS, indent=4))

    for url in vacc_urls:
        r = requests.get(url)
        json_data = json.loads(r.text)
        county = url.split('=')[-1]
        for entry in json_data['VaccineAdministration']:
            VACCINE.append(entry)
    
    base = Path()
    jsonpath = base / ("VACCINE.json")
    # base.mkdir(exist_ok=True)
    jsonpath.write_text(json.dumps(VACCINE, indent=4))
        # base = Path('VACCINE')
        # jsonpath = base / (county + ".json")
        # base.mkdir(exist_ok=True)
        # jsonpath.write_text(json.dumps(json_data, indent=4))
    
    r = requests.get(cli_url)
    json_data = json.loads(r.text)
    base = Path('CLI')
    jsonpath = base / ("GetResurgenceDataCLIAdmissions.json")
    base.mkdir(exist_ok=True)
    jsonpath.write_text(json.dumps(json_data, indent=4))



    




    print ("Done")
    
