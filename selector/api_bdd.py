#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:09:41 2019

@author: autre
"""

from flask import Flask
from flask_restful import Resource, Api
import scrap
import database
from datetime import datetime
import requests

app = Flask(__name__)
api = Api(app)

class bdd_insert(Resource):
    def get(self, hashtag):
        scrap.hashtag_to_bdd(hashtag)
        return {"uri": f"hashtag/{hashtag}"}

class bdd_retrieve(Resource):
    def get(self, hashtag):
        res = database.get_hashtag(hashtag)
        res["related_hashtags"] = database.get_related_hashtags(hashtag)
        if not res:
            return {"error": "hashtag not found", "hashtag": hashtag}
        for c in res:
            if isinstance(res[c], datetime):
                res[c] = datetime.isoformat(res[c])
        return res

class selector:
    def get(self,theme):
        hashtags=requests.get("/hashtag/"+theme) #est-ce que c'est comme ça qu'on fait appelle à bdd_retrieve ?
        #faudrait mettre une condition sur la popularité du hashtag
        return hashtags



api.add_resource(bdd_insert, '/insert/<string:hashtag>')
api.add_resource(bdd_retrieve, '/hashtag/<string:hashtag>')
api.add_resource(selector, '/selector/<string:theme>')


if __name__ == '__main__':
    app.run(debug=True, port=1997, host="0.0.0.0")