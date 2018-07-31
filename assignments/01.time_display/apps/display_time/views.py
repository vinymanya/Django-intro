# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.

# index method
def index(request):
	context = {
		"time": strftime("%a, %d %b %Y %H:%M %p", gmtime())  
	}
	return render(request, "display_time/index.html", context=context)
