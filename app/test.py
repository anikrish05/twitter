from flask import Flask, session,flash,render_template,redirect,url_for,jsonify
from datetime import datetime
import time
from flask import request
import json
from flask_pymongo  import PyMongo
from bson import json_util


app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/test")
def test():
	profiledb = mongo.db.profiles
	for i in range(1,100):
		profiledb.insert({"name":"Renga"+str(i),"userid":"rekannan"+str(i)})
		profiles = profiledb.find({},{"name":1,"_id":0})
		#print profiles
		#for p in profiles:
		#	print p
	return json_util.dumps(profiles, sort_keys=True, indent=4, default=json_util.default)



