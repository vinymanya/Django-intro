# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	return render(request, "amadon_site/index.html")

def buy(request, methods=["POST"]):
	# The logic goes here
	try:
		request.session["total_charged"]
	except KeyError:
		request.session["total_charged"] = 0

	try:
		request.session["total_items"]
	except KeyError:
		request.session["total_items"] = 0

	# request.session["total_charged"] += amount_charged
	request.session["total_items"] += int(request.POST["quantity"])
	# request.session["last_transaction"] = amount_charged
	return redirect("/checkout")

def checkout(request):
	return render(request, "amadon_site/checkout.html")
