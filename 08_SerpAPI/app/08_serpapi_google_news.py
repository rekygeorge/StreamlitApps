import serpapi
import os
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

results = client.search(
    engine='google_news',
    gl="in",    
    hl='en',
)

# data = results['reviews']

# print(results)

# print('Total reviews : ', len(results['reviews']))


# Pagination logic
# while 'serpapi_pagination' in results:
#     results = client.search(
#         engine='google_play_product',
#         product_id='com.chesskid',
#         store='apps',
#         all_reviews='true',
#         num=199,
#         next_page_token=results['serpapi_pagination']['next_page_token']
#     )
#     print('Total reviews : ', len(results['reviews']))

# print('all done')
    

for item in results['news_results']:
    # print(item)
    # print(item['highlight']['title'])
    print(item.get('highlight'))
    # print(item[1]['source']['link'])
    # print(item[1]['source']['date'])

    # for i in item:
    #     print(i)
    print('----------------------------------------')

# df = pd.DataFrame(data)
# df.to_csv('chess_reviews.csv', index=False)