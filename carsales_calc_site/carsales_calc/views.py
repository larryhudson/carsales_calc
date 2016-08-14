from django.shortcuts import render
from django import forms
from django.utils import timezone

from .forms import SearchForm

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
	else:
		form = SearchForm()

	return render(request, "search.html", {'form': form})

# def results(request):
# 	# list of results
# 
# 
# 
# def averages(request):
# 	# calculated averages from results
# 	
# 	# graphs?
