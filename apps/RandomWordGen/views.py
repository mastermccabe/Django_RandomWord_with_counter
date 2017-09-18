from django.shortcuts import render, HttpResponse, redirect
import re
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random, string



# from models import *
# the index function is called when root is visited
def index(request):
    # if not 'count' in session:
    if request.method == 'GET':
        if 'counter' not in request.session:
            request.session['counter']=0

    else:
        request.session['counter'] += 1
        # else:
        # count += 1
        letters = string.ascii_lowercase


        context = {
        "word":''.join(random.choice(letters) for i in range(14))}
        return render(request,'RandomWordGen/index.html', context)

    # print session['counter']

    return render(request,'RandomWordGen/index.html')


def reset(request):
    request.session['counter']=0
    return render(request,'RandomWordGen/index.html')
# def new(request):
