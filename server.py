from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json
import pymongo
import requests
import time

app = Bottle(__name__)

client = MongoClient('')
db = client.db_name

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers['Connection'] = 'keep-alive'

@app.route('/')
def root():
	return {'data': 'Server root'}

# @app.route('/led')
# def led():

# 	cur = db.led.find()
# 	data = json.loads(dumps(cur))
	
# 	return data[0]['val']

# @app.route('/led/<val>')
# def led(val):

# 	cur = db.led.update({"_id": ObjectId("")}, {'$set': {'val': str(val)}})

# 	return "LED Val: " + str(val)