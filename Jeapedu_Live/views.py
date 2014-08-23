#coding:utf-8
from django.shortcuts import render_to_response
from Jeapedu_Live.models import *
from django.template import RequestContext

def index(request):
	ind = Index.objects.all()[0]
	inde = Index.objects.all()
	d = {'ind':ind, 'inde':inde}
	return render_to_response('index.html', d, context_instance=RequestContext(request))

def courses(request):
	ind = Index.objects.all()[0]
	cou = Courses.objects.all()[0]
	d = {'cou':cou, 'ind':ind}
	return render_to_response('courses.html', d, context_instance=RequestContext(request))

def student(request):
	stu = Student.objects.all()[0]
	d = {'stu':stu}
	return render_to_response('student.html', d, context_instance=RequestContext(request))

def taped(request):
	ind = Index.objects.all()[0]
	tap = Taped.objects.all()[0]
	d = {'tap':tap, 'ind':ind}
	return render_to_response('taped.html', d, context_instance=RequestContext(request))

def live(request):
	ind = Index.objects.all()[0]
	liv = Live.objects.all()[0]
	d = {'liv':liv, 'ind':ind}
	return render_to_response('live.html', d, context_instance=RequestContext(request))

def ready(request):
	rea = Ready.objects.all()[0]
	d = {'rea':rea}
	return render_to_response('ready.html', d, context_instance=RequestContext(request))
