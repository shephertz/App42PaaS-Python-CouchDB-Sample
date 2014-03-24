from django.shortcuts import render
from django.conf import settings
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from couchdb import Server
from couchdb.client import *

SERVER = Server(getattr(settings,'COUCHDB_SERVER'))

if (len(SERVER) == 0):
    SERVER.create(getattr(settings,'COUCHDB_DATABASE'))

# Create your views here.

def index(request):
    return render_to_response('sample/index.html')
	

def detail(request):
    user = SERVER[getattr(settings,'COUCHDB_DATABASE')]
    if request.method == "POST":
        name = request.POST['name'].replace(' ','')
        description = request.POST['description'].replace(' ','')
        email = request.POST['email'].replace(' ','')
        user[name] = {'name':name,'email':email,'description':description}
        return HttpResponseRedirect(u"/show/")

def show(request):
    user = SERVER[getattr(settings,'COUCHDB_DATABASE')]
    lists = []
    for row in user:
        data = user[row]
        lists.append(data)			
    return render_to_response('sample/detail.html',{'lists':lists,'data':data})

