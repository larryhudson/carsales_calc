from selenium import webdriver
import xlsxwriter
import datetime
import configparser
driver = webdriver.Firefox()

user_make = "Toyota"
user_model = "Corolla"

# setup config file. if it exists, load it
config = configparser.ConfigParser()
if os.path.isfile('carsales_calc.ini'):
		config.read('carsales_calc.ini')
	user_settings = config["user"]
	user_state = user_settings["State"]
	user_transmission = user_settings["Transmission"]
	price_min, price_max = user_settings["Min price"], user_settings["Max price"]
	kms_min, kms_max = user_settings["Min kms"], user_settings["Max kms"]
else:
	config.add_section("user")
	user_settings = config["user"]
	print("Enter your State")
	user_state = input("> ")
	user_settings["State"] = user_state
	print("Enter your Transmission")
	user_transmission = input("> ")
	user_settings["Transmission"] = user_transmission
	print("Enter your price range separated by commas")
	user_price_range = input("> ")
	price_min, price_max = user_price_range.replace(' ','').split(",")
	user_settings["Min price"] = price_min
	user_settings["Max price"] = price_max
	print("Enter your KM range separated by commas")
	user_kms_range = input("> ")
	kms_min, kms_max = user_kms_range.replace(' ','').split(",")
	user_settings["Min kms"] = kms_min
	user_settings["Max kms"] = kms_max
	print("Saving config file.")
	with open('carsales_calc.ini', 'w') as configfile:
		config.write(configfile)

print("Enter car make and model")
car_choice = input("> ")

user_make, user_model = car_choice.split(" ")

print("Searching Carsales")
driver.get("http://www.carsales.com.au/cars/results?q=%28%28%28%28%28%28%28Make%3D%5B" + user_make + "%5D%26Model%3D%5B" + user_model + "%5D%29%26State%3D%5B" + user_state + "%5D%29%26Service%3D%5BCarsales%5D%29%26GenericGearType%3D%5B" + user_transmission + "%5D%29%26Price%3Drange%5B" + str(price_min) + ".." + str(price_max) + "%5D%29%26Odometer%3Drange%5B" + str(kms_min) + ".." + str(kms_max) + "%5D%29%26%28BodyStyle%3D%5BHatch%5D%7CBodyStyle%3D%5BSedan%5D%29%29&sortby=Year&limit=24")

pagination_div = driver.find_elements_by_css_selector("div.pagination")[0]
page_count = int(pagination_div.find_elements_by_tag_name("p")[0].text.split(' ')[1])
next_page_link = pagination_div.find_elements_by_partial_link_text("Next")[0].get_attribute('href')
current_page = 1
car_list = []

while current_page < page_count:
	print("Loading page", str(current_page))
	page_listings = driver.find_elements_by_css_selector("div.listing-item")
	real_page_listings = []
	for car in page_listings:
		if not "contentcards" in car.get_attribute('class'):
			real_page_listings.append(car)
	for car in real_page_listings:
		car_link = car.find_elements_by_tag_name('a')[0].get_attribute('href')
		car_title = car.find_elements_by_tag_name('h2')[0].text
		print("Adding", car_title)
		car_year = car_title.split(' ')[0]
		car_price = car.find_elements_by_css_selector('div.price')[0].text.replace('*)
		car_kms = car.find_elements_by_css_selector('div.feature-text')[0].text
		car_list.append([car_link, car_title, car_year, car_kms, car_price])
	pagination_div = driver.find_elements_by_css_selector("div.pagination")[0]
	next_page_link = pagination_div.find_elements_by_partial_link_text("Next")[0].get_attribute('href')
	driver.get(next_page_link)
	current_page += 1
	

# link, title, year, kms, price
now = datetime.datetime.now()
now_string = now.strftime("%d-%m-%y %H.%M")
workbook_filename = user_make + ' ' + user_model + ' ' + now_string + '.xlsx'
print("Creating spreadsheet", workbook_filename)
workbook = xlsxwriter.Workbook(workbook_filename)
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1})
url_format = workbook.add_format({'font_color': 'blue','underline': 1})


worksheet.write('A1', 'Link', bold)
worksheet.write('B1', 'Year', bold)
worksheet.write('C1', 'Kilometres', bold)
worksheet.write('D1', 'Price', bold)

row = 1
col = 0

for car in car_list:
	row = car_list.index(car) + 1
	worksheet.write_url(row, col, car[0], url_format, car[1])
	worksheet.write_string(row, col + 1, car[2])
	worksheet.write_string(row, col + 2, car[3])
	worksheet.write_string(row, col + 3, car[4])
print("Saving spreadsheet")
workbook.close()