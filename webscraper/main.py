import os, csv, json
from datetime import date
import requests
from copy import deepcopy

def getDataFromProvinceSpecificSites():

    today = date.today()
    formatted_date = today.strftime("%d-%m-%Y")
    formatted_date = "31-03-2020"
    # Get the data from the well hidden gov't location
    SECRET_URL = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"

    with requests.get(SECRET_URL,stream=True) as csv_contents:
        lines = (line.decode('utf-8') for line in csv_contents.iter_lines())

        prov_codes = {
            "10" : "NL", 
            "11": "PE", 
            "12": "NS", 
            "13": "NB", 
            "24": "QC", 
            "35": "ON", 
            "46": "MA", 
            "47": "SA", 
            "48": "AB", 
            "59": "BC", 
            "60": "YT", 
            "61" : "NT", 
            "62": "NU"
            }



        default_entry = {
                    'conf': 0,
                    'prob': 0,
                    'deaths': 0,
                    'total': 0,
                    'today': 0,
                    'percenttoday': 0,
                    'numtested': 0,
                    'daily': {}
                }

        data = {"Canada": deepcopy(default_entry), "PROVS": {}}
        for val in prov_codes.values():
            data["PROVS"][val] = deepcopy(default_entry)

        next(lines) # remove header

        for line in csv.reader(lines):



            if(line[0] not in prov_codes): #Canada is not a province
                # Represents all of Canada 

                if(line[3] == formatted_date):

                    data["Canada"] = {
                        'conf': line[4],
                        'prob': line[5],
                        'deaths': line[6],
                        'total': line[7],
                        'today': line[8],
                        'percenttoday': line[9],
                        'numtested': line[10],
                        'daily': data["Canada"]["daily"]
                        }

                data["Canada"]["daily"][line[3]] = {
                    'conf': line[4],
                    'prob': line[5],
                    'deaths': line[6],
                    'total': line[7],
                    'today': line[8],
                    'percenttoday': line[9],
                    'numtested': line[10]
                    }
            else:
                # Represents a province
                if(line[3] == formatted_date):
                    data["PROVS"][prov_codes[line[0]]] = {
                        'conf': line[4],
                        'prob': line[5],
                        'deaths': line[6],
                        'total': line[7],
                        'today': line[8],
                        'percenttoday': line[9],
                        'numtested': line[10],
                        'daily': data["PROVS"][prov_codes[line[0]]]["daily"]
                    }
                data["PROVS"][prov_codes[line[0]]]["daily"][line[3]] = {
                    'conf': line[4],
                    'prob': line[5],
                    'deaths': line[6],
                    'total': line[7],
                    'today': line[8],
                    'percenttoday': line[9],
                    'numtested': line[10]
                }   
        
        data["lastUpdate"] = formatted_date
        with open('covid-19.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)




if __name__ == '__main__':
    getDataFromProvinceSpecificSites()

