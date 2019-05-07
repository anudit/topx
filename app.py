import os
import requests
from dotenv import load_dotenv
load_dotenv()

APIKEY = os.environ.get("APIKEY")
CX =  os.environ.get("CX")
QUERY = "smile png"
X = 12

def getURLs(start = 0):  
    urlList = []
    
    URL = "https://www.googleapis.com/customsearch/v1?key="+APIKEY+"&cx="+CX+"&q="+QUERY if start !=0 else "https://www.googleapis.com/customsearch/v1?key="+APIKEY+"&cx="+CX+"&q="+QUERY+"&start="+str(start+1)
    r = requests.get(URL)
    res = r.json()
    items = res['items']

    for item in items:

        if('pagemap' in item and 'cse_image' in item['pagemap']):
            imageUrl = item['pagemap']['cse_image'][0]['src']
            urlList.append(imageUrl)

    return urlList

urlList = []
for i in range(0, X, 10):
    urlList += getURLs(i)

print(urlList[0:X])
