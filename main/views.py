#-*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.core.context_processors import request
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def home(request):
	return render_to_response( 'index.html' );
	