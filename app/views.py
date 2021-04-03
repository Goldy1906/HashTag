from django.shortcuts import render 
from django.views.static import serve
from .models import Getinfo
import mimetypes
from io import BytesIO
import os
import time
from django.http import HttpResponse
import sys
from subprocess import run, PIPE
# Create your views here.
def index(request):
    if request.method=="POST":
        getin=Getinfo()
        hashtag= request.POST.get('hashtag')
        tweetcount= request.POST.get('tweetcount')
        run([sys.executable,'E:\\project Shaky\\shaky\\dataset.py',hashtag,tweetcount], shell=False, stdout=PIPE)
        getin.hashtag=hashtag
        getin.tweetcount=tweetcount
        getin.save()
        # resp = download_file()
        context = {"data":"dataset"}
        return render(request,'index.html',context)
    return render(request, 'index.html')

def download(request, name):
    filepath = 'dataset.py'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
    
    







