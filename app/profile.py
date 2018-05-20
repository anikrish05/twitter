from flask import Flask, flash,render_template,redirect,url_for
import time
from flask import request
import json

app = Flask(__name__)
app.secret_key ='Anirudh'

@app.route("/getprofile") 

def getprofile():
	print ("I am in getprofiles")
	givenusername = request.args['foruser']

	print("*****************"+request.args['foruser'])

	profiles = json.load(open('profiles.json'))
	for profile in profiles['profiles']:
		if profile['cusername'] == givenusername:
			return render_template('profileview.html',profile=profile)
	return "Sorry not a valid user"
	#	data = json.load(json_filse	
	#	return json.dumps(data)


@app.route("/profile", methods=['GET','POST','Delete'])

def profile():
#	flash("Renga and Anirudh")
	if request.method == 'POST':
		print request.form.to_dict(flat=False)

		profiles = json.load(open('profiles.json'))
		for profile in profiles['profiles']:
			if profile['cusername']==request.form['cusername']:
				return("User name exists. invalid user name")
		


		profiles['profiles'].append(request.form.to_dict())
		with open('profiles.json','w') as outfile:
			json.dump(profiles,outfile)
		return redirect(url_for('getprofile',foruser=request.form['cusername']))
	elif request.method == 'GET':
		return render_template('profile.html')

	elif request.method == 'Delete':
		givenusername = request.args['foruser']
		profiles = json.load(open('profiles.json'))
		for profile in profiles['profiles']:
			profiles['profiles'].append(request.form.to_dict())
			with open('profiles.json','w') as outfile:
				json.dump(profiles,outfile)




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
		profiles = json.load(open('profiles.json'))

		print profiles['profiles']

		for profile in profiles['profiles']:
			#print(profile)
			if varusername== "Admin" and varpassword==  'Stanky123':
				return redirect(url_for('show_all'))
			elif profile['cusername'] == varusername and profile['cpassword'] == varpassword:
				return redirect(url_for('tweet',foruser=varusername))
		return "Wrong password"	

@app.route("/show_all")
def show_all():
	ctable = json.load(open('profiles.json'))

	return render_template('show_all.html',allprofiles=ctable)


@app.route("/tweet", methods=['GET','POST'])
def tweet():


	if request.method == 'GET':
		return render_template('tweet.html')
	elif request.method == 'POST':
		#username = request.args['foruser']
		print("Renga Kannan")
		print(request.form.to_dict())
		#vartweet=request.form['tweettext']
		#print(vartweet)
		tweets = json.load(open('tweets.json'))
		rjson = request.form.to_dict();
		rjson['username'] = "Renga"
		rjson['time'] ="05/10/2018:10:15"
		tweets['tweets'].append(rjson)
		with open('tweets.json','w') as outfile:
			json.dump(tweets,outfile)
		return("")