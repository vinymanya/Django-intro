# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
	return render(request, "new_words/index.html")

def session_process(request, methods=["POST"]):
	new_word = {}
	for key, value in request.POST.iteritems():
		if key != "csrfmiddlewaretoken" and key != "font":
			new_word[key] = value
		if key == "font":
			new_word["large"] = "large"
		else:
			new_word["large"] = ""
	new_word["created_at"] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")

	try:
		request.session["added_words"]
	except KeyError:
		request.session["added_words"] = []

	new_list = request.session["added_words"]
	new_list.append(new_word)
	request.session["added_words"] = new_list

	for key, val in request.session.__dict__.iteritems():
		print "*"*50
		print key, val 
		print "*"*50
	print "post created at", new_word
	return redirect("/")

def clear_session(request):
	# clear all keys in session
	for key in request.session.keys():
		del request.session[key]
	return redirect("/")

