#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:47:37 2019

@author: autre
"""

import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime

def connect():
    connection = psycopg2.connect(user = "user",
                              password = "user",
                              host = "192.168.33.10",
                              port = "5432",
                              database = "hashtagbdd")
    return connection
"""
connection=connect()
cursor = connection.cursor()
"""
# Print PostgreSQL Connection properties
#print ( connection.get_dsn_parameters(),"\n")

# Print PostgreSQL version
"""
cursor.execute("insert into hashtags(hashtag,popularity,nb_post_heure) values('sql',2113249,390)")
cursor.execute("SELECT * from hashtags;")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")
connection.commit()
connection.close()
cursor.close()
"""
def hashtag_to_bdd(hashtag):
    req= "http://best-hashtags.com/hashtag/"+hashtag
    page = requests.get(req)
    obj = BeautifulSoup(page.content)
    if len(obj.body.contents)==0:
        return
    #scrap hashtag
    hashtag_list_str=obj.find_all("div",class_="tag-box tag-box-v3 margin-bottom-40")[0].get_text(strip=True).replace('#','')
    hashtag_list=hashtag_list_str.split(" ")
    #print(hashtag_list[])
    
    #scrap popularity
    popularity=int(obj.find("div",class_="overflow-h").find_all("small")[1].get_text().replace(',',''))
    print(popularity)
    
    #scrap post_per_hour
    post_per_hour=int(obj.find_all("div",class_="overflow-h")[1].find_all("small")[1].get_text().replace(',',''))
    print(post_per_hour)
    
    connection=connect()
    cursor = connection.cursor()
    #cursor.execute("SELECT ha from hashtags;")
    cursor.execute("SELECT hashtag from hashtags where hashtag=%s;",(hashtag,))
    record = cursor.fetchone()
    #now=datetime.timestamp(datetime.now())
    #print(now)
    if record:
        cursor.execute("update hashtags set (popularity,nb_post_heure,last_update)=(%s,%s,now()) where hashtag=%s;",(popularity,post_per_hour,hashtag))
    else:
        cursor.execute("insert into hashtags(hashtag,popularity,nb_post_heure,last_update) values(%s,%s,%s,now())",(hashtag,popularity,post_per_hour))
        cursor.executemany("insert into related_hashtags(hashtag,relates_hashtag) values(%s,%s)", ((hashtag, rel_hashtag) for rel_hashtag in hashtag_list))
    
    
    
    connection.commit()
    connection.close()
    cursor.close()
    
    
hashtag_to_bdd("potato")
