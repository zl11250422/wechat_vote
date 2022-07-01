from django.shortcuts import render,HttpResponse,redirect
from django.http import StreamingHttpResponse,FileResponse, HttpResponse, JsonResponse
from django.core import serializers
from voteapp import models
from django import forms
import sys, os, subprocess, time, json, shutil, csv
import hashlib, struct
import numpy as np
# Create your views here.

def title(request):
    if request.method == "GET":
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    title = '你最喜欢的编程语言是？'
    query_title = models.DEMO_VOTE.objects.filter(title=title)
    if query_title.exists():
        pass        
    else:
        models.DEMO_VOTE.objects.create(title = title)    
    #vote_demo = models.DEMO_VOTE.objects.first().__dict__ #model转dict的一种方法，但会产生冗余的对象，不建议使用
    vote_demo = forms.model_to_dict(models.DEMO_VOTE.objects.first())
    vote_demo_detail = models.DEMO_VOTE_DETAIL.objects.all().values()
    vote_demo_detail = list(vote_demo_detail)
    #vote_demo = serializers.serialize('json', vote_demo)
    return JsonResponse({'vote_demo': vote_demo, 'vote_demo_detail': vote_demo_detail},json_dumps_params={'ensure_ascii':False},safe=False)

def submit(request):
    if request.method == "GET":
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    	
    detailId = request.params.dict()["ITEM"]
    openId = request.params.dict()["OPEN_ID"]
    result = models.DEMO_VOTE_RESULT.objects.filter(open_id=openId)
    RES = True
    if result.exists():
        RES = False        
    else:
        models.DEMO_VOTE_RESULT.objects.create(vote_id = 0, detail_id = detailId, open_id = openId)
        RES = True
    return JsonResponse({'RES': RES},json_dumps_params={'ensure_ascii':False},safe=False)

def result(request):
    if request.method == "GET":
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)
    openId = request.params.dict()["OPEN_ID"]
    current_vote = forms.model_to_dict(models.DEMO_VOTE_RESULT.objects.filter(open_id=openId).first())
    total_size = models.DEMO_VOTE_RESULT.objects.count()
    vote_demo_detail = models.DEMO_VOTE_DETAIL.objects.all().values()
    vote_demo_detail = list(vote_demo_detail)
    for i in range(len(vote_demo_detail)):
        vote_demo_detail[i]['size'] = models.DEMO_VOTE_RESULT.objects.filter(detail_id=vote_demo_detail[i]['id']).count()

    #voteId = request.params.dict()["VOTE_ID"]
    #openId = request.params.dict()["OPEN_ID"]
    #print(voteID)
    #print(openId)

    return JsonResponse({'total_size': total_size, 'vote_demo_detail': vote_demo_detail, 'current_vote': current_vote},json_dumps_params={'ensure_ascii':False},safe=False)