# 2 - Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".

import requests
response = requests.get("https://api.github.com")   # To Fetch data we will use .get function
print(response.json())   # Github api returns the data in json, and to parse json data into python data we will use .json() function here. 
