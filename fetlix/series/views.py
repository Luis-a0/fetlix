from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

class HelloWorld(View):
	
	def get(self, request):
		return HttpResponse(content=b'Hello World!')
		