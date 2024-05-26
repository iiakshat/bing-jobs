from bs4 import BeautifulSoup
import requests
import json

url = input("Paste URL from google jobs: ")
url = 'https://www.bing.com/jobs?q=ml+jobs&scp=0&rb=0&rc=20&L2=true&c=1&form=JOBL2S' if not url else url

page = requests.get(url).text

soup = BeautifulSoup(page, 'lxml')

jobs = soup.find_all('ul', class_='b_vList b_divsec b_loose')
i = 1
collection = {}

for job in jobs:
    date = job.find('div', class_='jb_postedDate').text

    if 'days' in date and int(date[:2])<=7:
        title = job.li.text
        com = job.find('div', class_='jbovrly_cmpny').text
        src = job.find('div', class_='jb_source').text
        des = job.find('div', class_='jbovrly_lj').text.split()
        loc = des[0]
        j_type = des[-1]

        jobid = f'Job {i}'
        i+=1

        collection[jobid] = {}
        collection[jobid]['Role'] = title
        collection[jobid]['Company'] = com
        collection[jobid]['Date'] = date
        collection[jobid]['Source'] = src[4:]
        collection[jobid]['Location'] = loc
        collection[jobid]['Job Type'] = j_type

with open("Jobs/jobs.json", "w") as f: 
    json.dump(collection, f, indent=4)