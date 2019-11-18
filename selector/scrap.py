#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:47:37 2019

@author: autre
"""

import requests
from bs4 import BeautifulSoup
import psycopg2



connection = psycopg2.connect(user = "user",
                              password = "user",
                              host = "192.168.33.10",
                              port = "5432",
                              database = "hashtagbdd")

cursor = connection.cursor()
# Print PostgreSQL Connection properties
print ( connection.get_dsn_parameters(),"\n")

# Print PostgreSQL version

cursor.execute("insert into hashtags(hashtag,popularity,nb_post_heure) values('technology',2113249,390)")
cursor.execute("SELECT * from hashtags;")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")
 

    
    
page = requests.get("http://best-hashtags.com/hashtag/muscle/")
obj = BeautifulSoup(page.content)
#print(obj.prettify)




def hashtag_to_bdd(hashtag):
    req= "http://best-hashtags.com/hashtag/"+hashtag
    page = requests.get(req)
    obj = BeautifulSoup(page.content)
    #print(obj.find_all("div",class_="tag-box tag-box-v3 margin-bottom-40")[0].get_text())
    
    
#hashtag_to_bdd("sql")