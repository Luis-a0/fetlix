from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib.auth import authenticate, login

class UserView(View):
	
	def get(self, request):
		return render(request, 'login.html')

	def post(self, request):
		user = authenticate(request, username=request.POST['name'], password=request.POST['password'])

		if user is not None:
			login(request, user)

			return HttpResponse(content=b'Sucess')
		return self.get(request)
		