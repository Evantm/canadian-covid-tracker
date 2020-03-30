import os, csv, json
from datetime import date

def getDataFromProvinceSpecificSites():

    today = date.today()
    formatted_date = today.strftime("%d-%m-%Y")
    print(formatted_date)
    
    # Get the data from the well hidden gov't location
    dataLocation = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"
    path = os.path.dirname(os.path.abspath(__file__))
    
    os.system("curl " + dataLocation + " > " + path + "/tmp/currentdata.csv" )

    # Process the CSV
    dataFile = open(path + "/tmp/currentdata.csv")
    rows = dataFile.readline().strip().split(',')

    prov_codes = {"1": "Canada", "10" : "NL", "11": "PE", "12": "NS", "13": "NB", "24": "QC", "35": "ON", "46": "MA", "47": "SA", "48": "AB", "59": "BC", "60": "YT", "61" : "NT", "62": "NU"}

    print(rows)

    data = {
        "Canada": {
            'conf': 0,
            'prob': 0,
            'deaths': 0,
            'total': 0,
            'today': 0,
            'percenttoday': 0,
            'numtested': 0,
            'daily': {}
        },
        "PROVS":{

            "BC": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}

            },
            "AB": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "SA": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "MA": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "ON": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "QC": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "NL": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "PE": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "NS": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "NB": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "YT": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "NT": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            },
            "NU": {
                'conf': 0,
                'prob': 0,
                'deaths': 0,
                'total': 0,
                'today': 0,
                'percenttoday': 0,
                'numtested': 0,
                'daily': {}
            }
        }
    }

    tempInd = 0
    for line in dataFile:
        current_line_data = line.strip().split(',')
    
        if(current_line_data[0] not in prov_codes):
            continue

        print(current_line_data)
        print(tempInd)
        tempInd = tempInd + 1

        if(current_line_data[0] == "1"):
            # Represents all of Canada 
            if(current_line_data[3] == formatted_date):
                data["Canada"] = {
                    'conf': current_line_data[4],
                    'prob': current_line_data[5],
                    'deaths': current_line_data[6],
                    'total': current_line_data[7],
                    'today': current_line_data[8],
                    'percenttoday': current_line_data[9],
                    'numtested': current_line_data[10],
                    'daily': data["Canada"]["daily"]
                }

            data["Canada"]["daily"][current_line_data[3]] = {
                'conf': current_line_data[4],
                'prob': current_line_data[5],
                'deaths': current_line_data[6],
                'total': current_line_data[7],
                'today': current_line_data[8],
                'percenttoday': current_line_data[9],
                'numtested': current_line_data[10]
            }
        else:
            # Represents a province
            if(current_line_data[3] == formatted_date):
                data["PROVS"][prov_codes[current_line_data[0]]] = {
                    'conf': current_line_data[4],
                    'prob': current_line_data[5],
                    'deaths': current_line_data[6],
                    'total': current_line_data[7],
                    'today': current_line_data[8],
                    'percenttoday': current_line_data[9],
                    'numtested': current_line_data[10],
                    'daily': data["PROVS"][prov_codes[current_line_data[0]]]["daily"]
                }
            print("writing to daily")
            data["PROVS"][prov_codes[current_line_data[0]]]["daily"][current_line_data[3]] = {
                'conf': current_line_data[4],
                'prob': current_line_data[5],
                'deaths': current_line_data[6],
                'total': current_line_data[7],
                'today': current_line_data[8],
                'percenttoday': current_line_data[9],
                'numtested': current_line_data[10]
            }   
    
    data["last-update"] = formatted_date
    result = json.dumps(data)

    writeable = open(path + "covid-19.json", "w")
    writeable.write(result)

    dataFile.close()
    writeable.close()

    print("Done")


getDataFromProvinceSpecificSites()

