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
from typing import Dict
from copy import deepcopy

app = Flask(__name__)
api = Api(app)

class bdd_insert(Resource):
    def get(self, hashtag):
        scrap.hashtag_to_bdd(hashtag)
        return {"uri": f"hashtag/{hashtag}"}

def datetime_to_string(d: Dict):
    """ Format all the datatime in a dict to iso format """
    res = deepcopy(d)
    for c in res:
        if isinstance(res[c], datetime):
            res[c] = datetime.isoformat(res[c])
    return res

class bdd_retrieve(Resource):
    def get(self, hashtag):
        res = database.get_hashtag(hashtag)
        res["related_hashtags"] = database.get_related_hashtags(hashtag)
        if not res:
            return {"error": "hashtag not found", "hashtag": hashtag}
        return datetime_to_string(res)

class selector(Resource):
    def get(self,theme):
        hashtags = database.get_related_hashtags(theme) #est-ce que c'est comme ça qu'on fait appelle à bdd_retrieve ?
        hashtags = {
            hashtag: datetime_to_string(database.get_hashtag(hashtag)) for hashtag in hashtags
        }
        #faudrait mettre une condition sur la popularité du hashtag
        return hashtags



api.add_resource(bdd_insert, '/insert/<string:hashtag>')
api.add_resource(bdd_retrieve, '/hashtag/<string:hashtag>')
api.add_resource(selector, '/selector/<string:theme>')


if __name__ == '__main__':
    app.run(debug=True, port=1997, host="0.0.0.0")