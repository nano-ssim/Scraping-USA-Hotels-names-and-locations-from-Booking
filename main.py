# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
import pandas as pd
import os
import glob

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

file_csv = open('Hotels_USA.csv', 'w', newline='')
header = ['Hotel name','Hotel location']
writer = csv.writer(file_csv, delimiter=',')
writer.writerow(header)
hotels = []

pages = np.arange(0, 1000, 25)

for p in pages:
    url = "https://www.booking.com/searchresults.fr.html?aid=301664&label=us-2d8n*MmBP5tLrDFWb1XEowS390613165571%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-1139564076%3Alp9069690%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YSNxgVPQVI7AMnn1KDvPMRs&sid=ff30ca9de8b639241405d2c59e63d632&tmpl=searchresults&class_interval=1&dest_id=224&dest_type=country&dtdisc=0&from_sf=50&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=country&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&src=searchresults&src_elem=sb&srpvid=d04d7cfd5cff01e2&ss=%C3%89tats-Unis&ss_all=0&ssb=empty&sshis=0&ssne=%C3%89tats-Unis&ssne_untouched=%C3%89tats-Unis&top_ufis=1&rows=25&offset=" + str(p)
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    ancher = soup.findAll('div',{'class' : 'sr_item_main_block'})

    for pt in  ancher:
       
       name = pt.find('span',{'class' : 'sr-hotel__name'})
       Location = pt.find('a',{'class' : 'bui-link'})
       data = [name.text.strip(),Location.text.replace('Indiquer sur la carte','').strip()]
       
       print(name.text.strip() +','+ Location.text.replace('Indiquer sur la carte','').strip())
      
      
       writer.writerow(data)
       csv_files = glob.glob('Hotels_USA.csv')
      
      
file_csv.close()

      

