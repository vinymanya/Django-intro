# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "surveys/index.html")


# process_form method
def process_form(request):
	# store input values in session
	request.session["name"] = request.POST["name"]
	request.session["dojo_location"] = request.POST["dojo_location"]
	request.session["fav_lang"] = request.POST["fav_lang"]
	request.session["comment"] = request.POST["comment"]
	return redirect("/surveys/result")

# Result route
def result(request):
	try:
		request.session["attempt"]
	except KeyError:
		request.session["attempt"] = 1
	else:
		 request.session["attempt"] += 1
	return render(request, "surveys/result.html")
