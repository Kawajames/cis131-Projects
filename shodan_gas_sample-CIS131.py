# File: shodan_gas_sample.py
# Desc: Shodan query for gas inv in AZ.
# Auth: Dakota Kartchner
# Date: 4/2/2025

import shodan
import json

SHODAN_API_KEY = 'fAuYSKAo3TmHaj7HK1JRSkIhdxBIPJCb'
api_object = shodan.Shodan(SHODAN_API_KEY)
search_query = "'in-tank inventory' state:'AZ'"

try:
  # Perform the search
  results = api_object.search(search_query)
  # Returns a dict with 'matches' and 'total'.
  matches = results.get("matches", [])
  # Loop over each match and print only the 'data' element.
  for match in matches:
    print(match.get("data", "No data found"))
    print("\n")
except shodan.APIError as error:
  # If there is an error with the call, print error.
  print("Error: {}".format(error))