import serpapi
import os
import csv

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)


results = client.search({
    'engine' : 'google_images',
    'q' : "cat",    # keyword
    'tbm' :'isch',  # isch : image search
    'gl':'us',      # geo location : country
    'ijn':0,       # image pagination
    'tbs':'isz:l,il:cl'
    
})

# print(results.keys())

with open('output_images.csv','w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Source', 'Thumbnail'])

    for result in results['images_results']:
        writer.writerow([result['title'], result['source'], result['thumbnail']])

print('Done writing to CSV file')
