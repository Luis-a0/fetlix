from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

class HelloWorld(View):
	
	def get(self, request):
		context = {
			'items': list(range(10))
		}
		return render(request, 'index.html', context=context)
		