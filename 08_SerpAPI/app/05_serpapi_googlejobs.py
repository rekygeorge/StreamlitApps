import serpapi
import os
import csv

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)


result = client.search({
    'engine' : 'google_jobs',
    'q' : "ignition scada programmer",   
    'location' :'New York, NY',  
    'chips':'date_posted:month',          
})


for job_result in result['jobs_results']:
    print(job_result['title'])
    print(job_result['company_name'])
    print(job_result['location'])
    print(job_result['detected_extensions'])


    highlights = job_result['job_highlights']
    for highlight in highlights:
        print(highlight)
    print('----------------------------------------')