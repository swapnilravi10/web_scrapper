from django.shortcuts import render
from .models import Webdata
# Create your views here.
import requests
requests.packages.urllib3.disable_warnings() #--> tp disable request warnings in console

from bs4 import BeautifulSoup

def scrape():
    session = requests.Session()
    session.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    url = 'https://www.flipkart.com/search?q=iphone+5s&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_0_7_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=iphone+5s&requestId=b7cd5a1d-5f60-45b7-9496-0d169b178380&as-backfill=on'
    content = session.get(url,verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    columns = soup.find_all('div',{'class':'_3O0U0u'})
    #print(len(columns))

    contain = columns[0]

    for contain in columns:
        product_name = contain.div.img["alt"]

        price_container = contain.find_all("div",{"class" : "_1vC4OE _2rQ-NK"})
        price = price_container[0].text.strip()
        rm_sep = ''.join(price.split(','))
        rm_rupee = rm_sep.split('₹')
        add_space = ''+rm_rupee[1]
        prices = add_space


        rating_container = contain.find_all("div",{"class" : "hGSR34"})
        rating = rating_container[0].text

            #print(product_name)
            #print(price)
            #print(rating)

        print(product_name.replace(",","|") + ", " + prices + ", " + rating + "\n")

        new_webdata = Webdata()
        new_webdata.name = product_name
        new_webdata.price = prices
        new_webdata.rating = rating
        new_webdata.save()
scrape()