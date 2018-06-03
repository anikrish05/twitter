from flask import Flask, session,flash,render_template,redirect,url_for
from datetime import datetime
import time
from flask import request
import json
from flask_pymongo  import PyMongo
from bson import json_util

app = Flask('twitter')
app.secret_key ='Anirudh'
mongo = PyMongo(app)

@app.route("/getprofile") 

def getprofile():
	#print ("I am in getprofiles")
	givenusername = request.args['foruser']
	profiledb = mongo.db.profiles

	profilec = profiledb.find({'cusername':givenusername})[0]
	if bool(profilec):
		print(json_util.dumps(profilec))
		return render_template('profileview.html',profile=profilec)
	else:
		return "Sorry Invalid User"


	#print("*****************"+request.args['foruser'])

	#profiles = json.load(open('profiles.json'))
	#for profile in profiles['profiles']:
	#	if profile['cusername'] == givenusername:
	#		return render_template('profileview.html',profile=profile)
	#return "Sorry not a valid user"
	#	data = json.load(json_filse	
	#	return json.dumps(data)


@app.route("/profile", methods=['GET','POST','Delete'])

def profile():
	profiledb = mongo.db.profiles

	if request.method == 'POST':
		#print(request.form.to_dict(flat=False))
		
		userc = profiledb.find({'cusername':request.form['cusername']})
		
		if userc.count() <> 0:
			print(">>>>>>>>> This User already exists")
			return("User name exists. invalid user name")

		#profiles = json.load(open('profiles.json'))
		#for profile in profiles['profiles']:
		#	if profile['cusername']==request.form['cusername']:
		#		return("User name exists. invalid user name")
		


		#profiles['profiles'].append(request.form.to_dict())
		
		input = request.form.to_dict()
		print(input)
		profiledb.insert(input)

		profilesc = profiledb.find({},{'_id':0,'name':1,'age':1,'lname':1,'mail':1,'cusername':1,'cpassword':1})
		print(json_util.dumps(profilesc, sort_keys=True, indent=4, default=json_util.default))

		#with open('profiles.json','w') as outfile:
		#	json.dump(profiles,outfile)
		return redirect(url_for('getprofile',foruser=request.form['cusername']))
	elif request.method == 'GET':
		return render_template('profile.html')

	elif request.method == 'Delete':
		givenusername = request.args['foruser']
		userc = profiledb.find({'cusername':givenusername})
		if userc.count() <> 0:
			print("Found the user")
		else:
			print("User is not a valid one")
		profiledb.deletemany({'cusername':givenusername})

		#profiles = json.load(open('profiles.json'))
		#for profile in profiles['profiles']:
		#	profiles['profiles'].append(request.form.to_dict())
		#	with open('profiles.json','w') as outfile:
		#		json.dump(profiles,outfile)




@app.route("/index")

def index():

	if request.method == 'GET': 
		return render_template('index.html')


@app.route("/about")

def about():
	return render_template('aboutus.html')
	
@app.route("/login", methods=['GET','POST'])


def login():

	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		varusername=request.form['eusername']
		varpassword=request.form['epassword']

		profiledb = mongo.db.profiles

		profilec = profiledb.find({'cusername':varusername,'cpassword':varpassword})
		if profilec.count() <> 0:
			session['username'] = varusername
			profileall = list(profiledb.find())
			if varusername == 'Admin':
				return redirect(url_for('show_all'))
			else:
				return render_template('Tweethome.html',allprofiles=profileall)


		else:
			return "Wrong user name or password"
		#profiles = json.load(open('profiles.json'))

		#print(profiles['profiles'])

		#for profile in profiles['profiles']:
			#print(profile)
		#	if varusername== "Admin" and varpassword==  'Stanky123':
		#		return redirect(url_for('show_all'))
		#	elif profile['cusername'] == varusername and profile['cpassword'] == varpassword:
		#		session['username'] = varusername
		#		ctable = json.load(open('profiles.json'))
		#		return render_template('Tweethome.html',allprofiles=ctable)
		#return "Wrong password"	

@app.route("/show_all")
def show_all():
	#ctable = json.load(open('profiles.json'))
	profiledb = mongo.db.profiles
	profileall = list(profiledb.find())
	print(profileall)

	return render_template('show_all.html',allprofiles=profileall)


@app.route("/tweet", methods=['GET','POST'])
def tweet():

## This is Renga's modification
## This is Renga's modification
	tweetdb = mongo.db.tweets
	if request.method == 'GET':
		return render_template('tweet.html')
	elif request.method == 'POST':
		#username = request.args['foruser']
		#print("Renga Kannan")
		#print(request.form.to_dict())
		#vartweet=request.form['tweettext']
		#print(vartweet)
	#	tweets = json.load(open('tweets.json'))
		rjson = request.form.to_dict();
		rjson['username'] = session['username']
		rjson['time'] =datetime.now().strftime('%m/%d/%Y:%H:%M')
		tweetdb.insert(rjson)
#		with open('tweets.json','w') as outfile:
#			json.dump(tweets,outfile)
		return redirect(url_for('tweethome'))

@app.route("/tweethome", methods=['GET'])
def tweethome():
	return render_template('tweethome.html')

@app.route("/feeds", methods=['GET'])
def feeds():
	#tweetsfile = json.load(open('tweets.json'))
	tweetsdb = mongo.db.tweets
	tweetsc   = list(tweetsdb.find())
	return render_template('Feeds.html',tweets=tweetsc)

@app.route("/follow",methods=['GET','POST'])
def follow():
	profiledb = mongo.db.profiles
	if request.method == 'GET':
		profileall = list(profiledb.find())
		print(profileall)
		return render_template('Follow.html',users=profileall)
	elif request.method == 'POST':
		print(request.form.to_dict())
		rjson = {}
	#	rjson['']