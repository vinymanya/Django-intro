# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

# Index method
def index(request):
	response = "placeholder to later display all the list of blogs"
	return HttpResponse(response)


# new method
def new(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

# Create method
def create(request):
	return redirect("/")

# Show method with url parameter
def show(request, number):
	response = "placeholder to display blog {}".format(number)
	return HttpResponse(response)

# Edit method
def edit(request, blog_number):
	response = "'placeholder to edit blog {}".format(blog_number)
	return HttpResponse(response)

# # Destroy method
# def destroy(request):
# 	return redirect("/")




