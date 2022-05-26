import requests
import json
import pymongo
from bs4 import BeautifulSoup as bf

def get_books_by_url():
    url = "https://cs.anjuke.com/sale/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    r = requests.get(url, headers=headers)
    html = r.content.decode("utf-8")
    soup = bf(html, 'lxml')

    #i = 0
    date = []
    name = []
    for ul in soup.select('#houselist-mod-new .list-item'):

        for a in (ul.select('.house-details .house-title')):
            #print(a.a.string)
            #date.append(a.a.string)
            date.append(a.a.attrs['title'])
        for d in (ul.select('.house-details .details-item')[0]):
            #hous_d = d.span.string
            #hous_det = list(hous_d)
            hous_d = d.string

            print(hous_d.split('|',1))

        for b in(ul.select('.pro-price .price-det')):
            #print(b.strong.string)
            date.append(b.strong.string)

        for c in (ul.select('.pro-price .unit-price')):
            #print(c.string)
            date.append(c.string)
    #date1 = json.loads(date.content.decode("utf-8"))

    for i in range(len(date)):
        b = 'house'+str(i+1)
        name.append(b)
    #print(len(name))

    d = dict(zip(name,date))
    #d = [name,date]
    print(d)
'''
    client = pymongo.MongoClient()
    db = client['house']
    details = db["data"]
    x = details.insert_one(d)
    print(x)
'''
    #return data
get_books_by_url()