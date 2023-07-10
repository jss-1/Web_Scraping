from bs4 import BeautifulSoup
import requests
import time

print('Print some skill you are not familiar with')
unfamiliar_skill=input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        pub_date=job.find('span', class_='sim-posted').span.text
        if 'few' in pub_date:
            skills=job.find('span', class_='srp-skills').text.replace(' ','')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    comp_name=job.find('h3', class_='joblist-comp-name').text.replace(' ','')
                    link=job.header.h2.a['href']
                    f.write(f'Company Name: {comp_name.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f'Publish Date: {pub_date.strip()}\n')
                    f.write(f'Link: {link.strip()}')
                print(f'files saved:{index}')
            print('')

if __name__=='__main__':
    while True:
        find_jobs()
    time.sleep(30)
