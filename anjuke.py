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
    for ul in soup.select('#houselist-mod-new .list-item'):

        for a in (ul.select('.house-details .house-title')):
            #print(a.a.string)
            date.append(a.a.string)

        for b in(ul.select('.pro-price .price-det')):
            #print(b.strong.string)
            date.append(b.strong.string)

        for c in (ul.select('.pro-price .unit-price')):
            #print(c.string)
            date.append(c.string)
    #date1 = json.loads(date)
    for i in range(len(date)):
        print('Date print:',date[i])
        """
        answer_table = [ul.select('.house-details .details-item')[0] for x in ul if
                        ul.string is not None]
        """
        #print(type(answer_table))
        #print(i)
        #print(answer_table[1])
        #i = i + 1

        """
        for dt in (ul.select('.house-details .details-item')[0]):
            #print(type(dt))
            if type(dt.string) is not None :
                print(dt.string)
            #print(dt.string)
            #print(dt.string)
        """

    #return data
get_books_by_url()