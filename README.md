# carsales_calc
Python script that scrapes Carsales.com.au to  generate a spreadsheet showing the resale value of a car. Also working on a Django site that will do a similar thing.

# What it does
* Creates a config file for preferred settings: State, Transmission, Price range, Kms range
* Populates list of search results with the car's link, price, year, kms
* Generates a Matplotlib scatter plot graph showing how price declines as the car's year goes down

![Example](img/example.png?raw=true "X-axis is year, Y-axis is price")



# To do list
* Generate graph to show resale value
* Compare each car to the average, to show which ones are good deals
* Add RWC / Rego search
* Recreate selenium-webdriver functionality with BeautifulSoup for Django
* Add stuff like recent searches, popular cars to Django homepage
* Maybe add Bootstrap theme?
