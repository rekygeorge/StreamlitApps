import serpapi
import os
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

results = client.search(
    engine='google_play_product',
    product_id="com.chesskid",    
    store='apps',
    all_reviews='true',
    num=199,
)

data = results['reviews']

print(results)

print('Total reviews : ', len(results['reviews']))


# Pagination logic
while 'serpapi_pagination' in results:
    results = client.search(
        engine='google_play_product',
        product_id='com.chesskid',
        store='apps',
        all_reviews='true',
        num=199,
        next_page_token=results['serpapi_pagination']['next_page_token']
    )
    print('Total reviews : ', len(results['reviews']))

print('all done')
    

# for item in results['organic_results']:
#     print(item['title'])
#     print(item['link'])
#     print(item['snippet'])
#     print('----------------------------------------')

df = pd.DataFrame(data)
df.to_csv('chess_reviews.csv', index=False)