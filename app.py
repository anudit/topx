import os
import requests
from dotenv import load_dotenv
load_dotenv()

APIKEY = os.environ.get("APIKEY")
CX =  os.environ.get("CX")
QUERY = "smile png"

URL =  "https://www.googleapis.com/customsearch/v1?key="+APIKEY+"&cx="+CX+"&q="+QUERY+"&start=10"
r = requests.get(URL)
res = r.json()
items = res['items']

for item in items:
    pagemap = item['pagemap']
    if('cse_image' in pagemap):
        imageUrl = pagemap['cse_image'][0]['src']
        print(imageUrl)
        print("\n")