from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dotenv import load_dotenv
import pyrebase
import os

load_dotenv()
print('--------')

config = {
  "apiKey" : os.getenv('API_KEY'),
  "authDomain": os.getenv('AUTH_DOMAIN'),
  "databaseURL": "",
  "projectId": os.getenv('PROJECT_ID'),
  "storageBucket": os.getenv('STORAGE_BUCKET'),
  "messagingSenderId": os.getenv('MESSAGING_SENDER_ID'),
  "appId": os.getenv('APP_ID'),
}

# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def signIn(request):
	return render(request,"robotchildren/login.html")

def postsignIn(request):
	email=request.POST.get('email')
	pasw=request.POST.get('pass')
	try:
		# if there is no error then signin the user with given email and password
		user=authe.sign_in_with_email_and_password(email,pasw)
	except:
		message="Invalid Credentials!!Please Check your Data"
		return render(request,"robotchildren/login.html",{"message":message})
	session_id=user['idToken']
	request.session['uid']=str(session_id)
	return render(request,"robotchildren/index.html",{"email":email})

def logout(request):
	try:
		del request.session['uid']
	except:
		pass
	return render(request,"robotchildren/login.html")

def signUp(request):
	return render(request,"robotchildren/registration.html")

def postsignUp(request):
	email = request.POST.get('email')
	passs = request.POST.get('pass')
	name = request.POST.get('name')
	try:
		# creating a user with the given email and password
		user=authe.create_user_with_email_and_password(email,passs)
		uid = user['localId']
		idtoken = request.session['uid']
		print(uid)
		print("uid successful")
	except:
		return render(request, "robotchildren/registration.html")
	return render(request,"robotchildren/login.html")
