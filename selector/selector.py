#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:26:32 2019

@author: autre
"""

#voici selector.py l'endroit ou les hashtags sont choisis
from flask import Flask
from flask_restful import Resource, Api
import scrap
import database
from datetime import datetime
import requests

app = Flask(__name__)
api = Api(app)

class selector:
    def get_perfect_hashtags(theme,detect):
        hashtags=requests.get("/hashtag/"+theme) #est-ce que c'est comme ça qu'on fait appelle à bdd_retrieve ?
        #faudrait mettre une condition sur la popularité du hashtag
        return hashtags
    
api.add_resource(get_perfect_hashtags, '/select/<string:theme>/<string:detect>')

if __name__ == '__main__':
    app.run(debug=True, port=1998, host="0.0.0.0")