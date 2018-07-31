# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "Hello this is my first Django app"
	return HttpResponse(response)

def test(request):
	response = "Hello I am test"
	return HttpResponse(response)

def publish_year(request, year):
	response = "The article was published in {}".format(year)
	return HttpResponse(response)
