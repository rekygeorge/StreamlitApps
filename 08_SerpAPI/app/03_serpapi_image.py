import serpapi
import os
import csv

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)


result = client.search({
    'engine' : 'google_images',
    'q' : "cat",    # keyword
    'tbm' :'isch',  # isch : image search
    'gl':'us',      # geo location : country
    'ijn':'1'       # image pagination
    
})


for item in result['images_results']:
    print(item['title'])
    print(item['source'])
    print(item['thumbnail'])
    print('----------------------------------------')