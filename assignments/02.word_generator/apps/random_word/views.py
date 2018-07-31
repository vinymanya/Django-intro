# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Function that generate and return random word
def random_word(n):
	# You can optionally specify allowed characters.
	random_word = get_random_string(length=n, allowed_chars='#$%^&890HDGFTRYE68565') 
	return random_word

# Create your views here.
def index(request):
    try:
        request.session['attempt']
    except KeyError:
        request.session['attempt'] = 0
    return render(request, "random_word/index.html")

def generate(request):
    request.session['attempt'] += 1  
    request.session['word'] = random_word(14)
    return redirect('/')

def reset(request):
    del request.session['attempt']
    del request.session['word']
    return redirect('/')




