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

class initdb(Resource):
    def get(self):
        conn = scrap.connect()
        cursor = conn.cursor()
        cursor.execute("""
create table hashtags(
	hashtag varchar(255) primary key,
	popularity int,
	nb_post_hour int,
	last_update timestamp
);

create table related_hashtags(
	hashtag varchar(255) references hashtags(hashtag),
	relates_hashtag varchar(255)
);
        """)
        cursor.close()
        conn.commit()
        conn.close()
        return {"success": True}

api.add_resource(bdd_insert, '/insert/<string:hashtag>')
api.add_resource(initdb, '/initdb')

if __name__ == '__main__':
    app.run(debug=True, port=1997, host="0.0.0.0")