import re
import os
import time
import requests
from trafilatura import extract
from bs4 import BeautifulSoup

#the source url where to get a list of physics related urls
source_url= requests.get('https://en.wikipedia.org/wiki/Outline_of_physics')
max_urls=10
wait_seconds=15
save_path= '../../data/raw'

#get list of urls
soup = BeautifulSoup(source_url.text, 'html.parser')
 
urls = []
slash_patter=r"^/wiki/"
for link in soup.find_all('a'):
    temp_link= link.get('href')
    if re.search(slash_patter, temp_link):
        urls.append('https://en.wikipedia.org'+link.get('href'))
urls= list(set(urls))

for i in range(max_urls):
    i_title= urls[i].split('/')[-1].lower().replace(' ', '')
    i_text= requests.get(urls[i])
    i_text= extract(i_text.text)
    i_text= i_text.lower()
    #get rid of see also and external references
    i_text= i_text[:i_text.find('see also')]
    text_file = open(os.path.join(save_path,i_title+'.txt'), "w")
    text_file.write(i_text)
    text_file.close()
    time.sleep(wait_seconds)
   

