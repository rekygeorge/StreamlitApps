import serpapi
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

result = client.search(
    q="python programming language",
    engine='google',
    location='Austin, Texas',
    hl='en'
)

print(result)

for item in result['organic_results']:
    print(item['title'])
    print(item['link'])
    print(item['snippet'])
    print('----------------------------------------')