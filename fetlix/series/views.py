from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic.base import View

from series.models import Serie, Episode

class SerieView(View):
	
	def get(self, request):
		if request.user.is_authenticated:
			context = {
				'series': list(Serie.objects.all())
			}
			return render(request, 'series.html', context=context)
		return Http404()

class EpisodeView(View):
	
	def get(self, request, serie_id: int):
		if request.user.is_authenticated:
			context = {
				'episodes': list(Episode.objects.filter(serie_id=serie_id))
			}
			return render(request, 'episodes.html', context=context)
		return Http404()
		