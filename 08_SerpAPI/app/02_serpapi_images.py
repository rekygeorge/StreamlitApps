import serpapi
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

endOfPage = False
pageNr = 0


while not endOfPage:
    results = client.search({
        'engine' : 'google_images',
        'q' : "cat",    # keyword
        'tbm' :'isch',  # isch : image search
        'gl':'us',      # geo location : country
        'ijn':pageNr       # image pagination
        
    })

    if results['search_information']['image_results_state'] == 'Fully empty':
        endOfPage = True
        print('End of Page')
        break

    pageNr += 1
    # endOfPage = result['serpapi_pagination']['next_page'] == False
    print('first result : ', results['images_results'][0]['title'])


    # print(result)

    # for item in result['images_results']:
    #     print(item['title'])
    #     print(item['source'])
    #     print(item['thumbnail'])
    #     print('----------------------------------------')