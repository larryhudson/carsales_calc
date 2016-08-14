from django import forms
from .models import Search

class SearchForm(forms.ModelForm):
	class Meta:
		model = Search
		fields = ("car_make", "car_model", "transmission", "min_price", "max_price", "min_kms", "max_kms", "state")