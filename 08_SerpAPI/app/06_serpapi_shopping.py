import serpapi
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

results = client.search(
    engine='google_shopping',
    q="cat food",
    tbs='mr:1,price:1,ppr_min:7,ppr_max:10,pdtr0:951440%7C951446',
    hl='en'
)

print(results)

for item in results['shopping_results']:
    print(item['title'])
    print(item['price'])
    print(item['product_link'])
    print(item['product_id'])
    print(item['rating'])
    print('----------------------------------------')