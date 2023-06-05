#!/usr/bin/env pyt
# coding: utf-8 
#----------------------------------------------------------------------------
# Created By  : thaislba
# Created Date: 04/06/2023
# version ='1.0'

import requests
import json
import sys
import time

def get_breweries(page_size:int) -> None: 
	"""
      Call OpenBrewery APY GET method and populates a file with the data returned.
      Argumentos:
		  page_size: amount of json returned in the API page
      Retorna:
          N/A

    """

	i = 0
	#creates a file with the time of the processing
	timestr = time.strftime("%d%m%Y-%H%M%S")
	f = open(timestr + "_data.txt", "a")
	while True:
		try:
			#object Response r that will contain the information returned by the URL
			endpoint = "https://api.openbrewerydb.org/v1/breweries?page="+str(i)+"&per_page="+str(page_size)+""
			r = requests.get(endpoint)
			if(len(r.json()) != 0):
				f.write(r.text + ",\n")
				i += 1
			else:
				break
		except Exception as e:
			print("An exception occurred")
			print(e)

def main():
	
	get_breweries(50)
	metadata = requests.get("https://api.openbrewerydb.org/v1/breweries/meta")
	print(metadata.json())
	sys.exit(0)

if __name__ == '__main__':
    main()
