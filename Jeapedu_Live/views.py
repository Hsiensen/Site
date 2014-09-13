#coding:utf-8
from django.shortcuts import render_to_response
from Jeapedu_Live.models import *
from django.template import RequestContext

def index(request):
	inde = Index.objects.all()
	d = {}
	if len(inde):
		d['ind'] = ind[0]
		d['inde'] = inde
	alltext = TextInfo.objects.all()
	allimg = ImgInfo.objects.all()
	for text in alltext:
		d[text.tagname] = text.text
	for img in allimg:
		d[img.tagname] = img.image
	return render_to_response('index.html', d, context_instance=RequestContext(request))

def courses(request):
	ind = Index.objects.all()
	cou = Courses.objects.all()
	d = {}
	if len(ind):
		d['ind'] = ind[0]
	if len(cou):
		d['cou'] = cou[0]
	alltext = TextInfo.objects.all()
	allimg = ImgInfo.objects.all()
	for text in alltext:
		d[text.tagname] = text.text
	for img in allimg:
		d[img.tagname] = img.image
	return render_to_response('courses.html', d, context_instance=RequestContext(request))

def student(request):
	stu = Student.objects.all()
	d = {}
	if len(stu):
		d['stu'] = stu[0]
	alltext = TextInfo.objects.all()
	allimg = ImgInfo.objects.all()
	for text in alltext:
		d[text.tagname] = text.text
	for img in allimg:
		d[img.tagname] = img.image
	return render_to_response('student.html', d, context_instance=RequestContext(request))

def taped(request):
	ind = Index.objects.all()
	tap = Taped.objects.all()
	d = {}
	if len(ind):
		d['tap'] = tap[0]
	if len(tap):
		d['ind'] = ind[0]
	alltext = TextInfo.objects.all()
	allimg = ImgInfo.objects.all()
	for text in alltext:
		d[text.tagname] = text.text
	for img in allimg:
		d[img.tagname] = img.image
	return render_to_response('taped.html', d, context_instance=RequestContext(request))

def live(request):
	ind = Index.objects.all()
	liv = Live.objects.all()
	d = {}
	if len(ind):
		d['liv'] = liv[0]
	if len(liv):
		d['ind'] = ind[0]
	alltext = TextInfo.objects.all()
	allimg = ImgInfo.objects.all()
	for text in alltext:
		d[text.tagname] = text.text
	for img in allimg:
		d[img.tagname] = img.image
	return render_to_response('live.html', d, context_instance=RequestContext(request))

def ready(request):
	rea = Ready.objects.all()
	d = {}
	if len(rea):
		d['rea'] = rea[0]
	alltext = TextInfo.objects.all()
	allimg = ImgInfo.objects.all()
	for text in alltext:
		d[text.tagname] = text.text
	for img in allimg:
		d[img.tagname] = img.image
	return render_to_response('ready.html', d, context_instance=RequestContext(request))
