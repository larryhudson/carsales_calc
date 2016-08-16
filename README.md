# carsales_calc
Python script that scrapes Carsales.com.au to  generate a spreadsheet showing the resale value of a car. Also working on a Django site that will do a similar thing.

# What it does
* Creates a config file for preferred settings: State, Transmission, Price range, Kms range
* Populates list of search results with the car's link, price, year, kms
* Writes each to an Excel spreadsheet
* Records average price for each year (in second sheet)

# To do list
* Generate graph to show resale value
* Compare each car to the average, to show which ones are good deals
* Add RWC / Rego search
* Recreate selenium-webdriver functionality with BeautifulSoup for Django
* Add stuff like recent searches, popular cars to Django homepage
* Maybe add Bootstrap theme?
