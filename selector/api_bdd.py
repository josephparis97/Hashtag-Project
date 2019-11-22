#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:09:41 2019

@author: autre
"""

from flask import Flask
from flask_restful import Resource, Api
import scrap



app = Flask(__name__)
api = Api(app)

class bdd_insert(Resource):
    def get(self,hashtag):
        return scrap.hashtag_to_bdd(hashtag)

api.add_resource(bdd_insert, '/insert/<string:hashtag>')

if __name__ == '__main__':
    app.run(debug=True)