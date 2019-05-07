import os
import requests
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()

APIKEY = os.environ.get("APIKEY")
CX =  os.environ.get("CX")
QUERY = "smile png"

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

def getUrlList(X):
    urlList = []
    # print("Processing Pages:")
    for i in tqdm(range(0, X, 10), desc="Processing Pages"):
        urlList += getURLs(i)
    return urlList[0:X]

# def storeFiles():

print(getUrlList(12))
