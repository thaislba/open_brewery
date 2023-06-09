# coding: utf-8 
#----------------------------------------------------------------------------
# Created By  : thaislba
# Created Date: 04/06/2023
# version ='1.0'

import requests
import json
import sys
import ndjson

def get_breweries(page_size:int) -> None: 
	"""
      Call OpenBrewery API GET method and populates a file with the data returned.
      Argumentos:
		  page_size: amount of json returned in the API page
      Retorna:
          N/A

    """
    
	file_name = "/opt/scripts/brewery_data/brewery.csv"
	f = open(file_name, "w")
	f.write("")
	f.close()
	f = open(file_name, "a")
	i=0
	while True:
		try:
			endpoint = "https://api.openbrewerydb.org/v1/breweries?page="+str(i)+"&per_page="+str(page_size)+""
			#object Response r that will contain the information returned by the URL
			r = requests.get(endpoint)
			if(len(r.json()) != 0):
				#f = open(file_name, "a")
				data = json.loads(r.text)
				data_formatted = ndjson.dumps(data)
				f.write(data_formatted+"\r\n")
				print("que")
				i += 1
			else:
				break
		except Exception as e:
			print("An exception occurred")
			print(e)
			break
	f.close()	

def main():
	
	get_breweries(50)
	metadata = requests.get("https://api.openbrewerydb.org/v1/breweries/meta")
	print(metadata.json())
	sys.exit(0)

if __name__ == '__main__':
    main()
