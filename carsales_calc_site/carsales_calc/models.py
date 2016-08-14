from django.db import models
from django.utils import timezone

# Create your models here.

class Search(models.Model):
	car_make = models.CharField(max_length=25)
	car_model = models.CharField(max_length=25)
	search_date = timezone.now()
	
	# transmission - auto / manual
	AUTO = 'Automatic'
	MAN = 'Manual'
	
	transmission_choices = (
	    (AUTO, 'Automatic'),
	    (MAN, 'Manual')
	)
	transmission = models.CharField(
	    choices=transmission_choices,
	    max_length=10
	)
	# min price
	min_price = models.IntegerField(default=0)
	# max price
	max_price = models.IntegerField(default=0)
	# min kms
	min_kms = models.IntegerField(default=0)
	# max kms
	max_kms = models.IntegerField(default=0)
	# State
	ACT = 'ACT'
	NSW = 'New South Wales'
	NT = 'Northern Territory'
	QLD = 'Queensland'
	SA = 'South Australia'
	TAS = 'Tasmania'
	VIC = 'Victoria'
	WA = 'Western Australia'
	
	state_choices = (
	    (ACT, 'ACT'),
	    (NSW, 'New South Wales'),
	    (NT, 'Northern Territory'),
	    (QLD, 'Queensland'),
	    (SA, 'South Australia'),
	    (TAS, 'Tasmania'),
	    (VIC, 'Victoria'),
	    (WA, 'Western Australia')
	)
	
	state = models.CharField(
	   max_length=25,
	   choices=state_choices
	)
	
	# search_url = "http://www.carsales.com.au/cars/results?q=%28%28%28%28%28%28%28Make%3D%5B"
# 	+ str(car_make) + "%5D%26Model%3D%5B" + str(car_model) + "%5D%29%26State%3D%5B" + str(state)
# 	+ "%5D%29%26Service%3D%5BCarsales%5D%29" + "%26GenericGearType%3D%5B" + str(transmission)
# 	+ "%5D%29" + "%26Price%3Drange%5B" + str(min_price) + ".." + str(max_price) + "%5D%29"
# 	+ "%26Odometer%3Drange%5B" + str(min_kms) + ".." + str(max_kms) + "%5D%29%26%28BodyStyle%3D%5BHatch%5D%7CBodyStyle%3D%5BSedan%5D%29%29&sortby=Year&limit=24"
	
	# search_string = str(car_make) + " " + str(car_model)	
# 	def __str__(self):
# 		return self.search_string

# class Car(models.Model):
# 	search = models.ForeignKey(Search,on_delete=models.CASCADE)
# 	car_make = models.ForeignKey
# 	car_model = models.ForeignKey
# 	transmission = models.ForeignKey
# 	price = models.IntegerField
# 	kms = models.IntegerField
# 	state = models.Foreignkey
	

