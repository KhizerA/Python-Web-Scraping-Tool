#https://realpython.com/beautiful-soup-web-scraper-python/
import requests
from bs4 import BeautifulSoup
import pandas
import sys

file = pandas.read_csv('C:/Users/khize/OneDrive/Desktop/Abu b2b/True North/Links.csv')
link_list = file['Link'].tolist()
master_l = []
master_p = []
master_d = []

for index, links in enumerate(link_list):
    product_list = []
    description_list = []
    URL = links
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='content')
    if results is None:
        continue
    job_elems = results.find_all('div', class_='sqs-block html-block sqs-block-html')

    for num, job_elem in enumerate(job_elems):
        list = []
        title = job_elem.find('h2')
        description = job_elem.find_all('p', class_='')
        if title is None:
            continue
        product_list.insert(num, title.get_text())

        for i, x in enumerate(description):
            if description[i] is None:
                continue
            list.insert(i, description[i].text)
        des_output = ', '.join(list)
        description_list.insert(num, des_output)

    master_p.extend(product_list)
    master_d.extend(description_list)
    for count in range(len(product_list)):
        master_l.append(links)

dictionary = {'Link': master_l, 'Product': master_p, 'Description': master_d}
df = pandas.DataFrame(dictionary)
df.to_csv('C:/Users/khize/OneDrive/Desktop/Abu b2b/True North/True North Scrape.csv')




