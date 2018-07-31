# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
	context = {
	"time": strftime("%a, %d %b %Y %H:%M %p", gmtime())
	}
	try:
		request.session["activities"]
	except KeyError:
		request.session["activities"] = []

	try:
		request.session["gold"]
	except KeyError:
		request.session["gold"] = 0
	return render(request, "ninja/index.html", context)

def process_money(request):
	#set up some logic to process money
	if request.POST["building"] == "farm":
		num_gold = random.randint(10, 20)
		request.session["gold"] += num_gold
		activity = "Earned " + str(num_gold) + " golds" + " from the farm"
		request.session["activities"].append(activity)
		return redirect("/")

	elif request.POST["building"] == "cave":
		num_gold = random.randint(5, 10)
		request.session["gold"] -= num_gold
		activity = "Lost " + str(num_gold) + " golds" + " from the cave"
		request.session["activities"].append(activity)
		return redirect("/")

	elif request.POST["building"] == "house":
		num_gold = random.randint(2, 5)
		request.session["gold"] += num_gold
		activity = "Earned " + str(num_gold) + " golds" + " from the house"
		request.session["activities"].append(activity)
		return redirect("/")

	elif request.POST["building"] == "casino":
		num_gold = random.randint(5, 10)
		request.session["gold"] -= num_gold
		activity = "Lost " + str(num_gold) + " golds" + " from the casino"
		request.session["activities"].append(activity)
		return redirect("/")
	return redirect("/")


# Clear session
def reset(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect("/")
