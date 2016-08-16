from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.utils import timezone
from django.http import HttpResponse, Http404

from .forms import SearchForm
from .models import Search, Car
from . import calc_function


# def index(request):
# 	# most popular cars?
# 	
# 	# recent searches?
# 	
def search(request):
	# fields for search
	
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():

			# commit=False means the form doesn't save at this time.
			# commit defaults to True which means it normally saves.
			model_instance = form.save(commit=False)
			model_instance.search_date = timezone.now()
			model_instance.save()
			return redirect('/carsales_calc/results/' + str(model_instance.id))
	else:
		form = SearchForm()

	return render(request, "search.html", {'form': form})

def results(request, pk):
	search = get_object_or_404(Search, pk=pk)
	car_list = Car.objects.filter(search=search)
	calc_function.add_car_objs(search.id)
	return render(request, 'results.html', {'search': search, 'car_list': car_list})
# def results(request):
# 	# list of results
# 
# 
# 
# def averages(request):
# 	# calculated averages from results
# 	
# 	# graphs?
