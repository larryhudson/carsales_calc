from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()

make = input("Enter car make: ")
model = input("Enter car model: ")
yearly_increment = int(input("Enter yearly increment: "))
year = 2013
prices = []

while year > 1999:
    driver.get("http://www.carsales.com.au/car-valuations/refine/" + make + "/" + model + "/" + str(year) + "/Automatic")
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, 200)")
    try:
        car_div = driver.find_element_by_css_selector("car-card.ng-scope")
        car_div2 = car_div.find_element_by_css_selector("div.hide-mobi")
        select_button = car_div2.find_element_by_tag_name("button")
        select_button.click()
        low_price = int(driver.find_element_by_css_selector("span.price-min").text.replace(",","").strip("$*"))
        high_price = int(driver.find_element_by_css_selector("span.price-max").text.replace(",","").strip("$*"))
        mid_price = (low_price + high_price) / 2
    except NoSuchElementException:
        mid_price = "none found"

    prices.append((year, mid_price))
    print("Year = {0}, average price = {1}".format(year, mid_price))
    year -= yearly_increment

comparison_increment = int(input("Enter comparison increment: "))

for tuple_index, tuple_thing in list(enumerate(prices[:-3])):
    current_year = tuple_thing[0]
    current_price = tuple_thing[1]
    earlier_year = prices[tuple_index + comparison_increment][0]
    earlier_price = prices[tuple_index + comparison_increment][1]
    difference_in_yrs = current_year - earlier_year
    if isinstance(earlier_price, float):
        drop_off = current_price - earlier_price
        print("Drop off in value for {0} car after {1} years: {2}".format(current_year, difference_in_yrs, drop_off))
    else:
        print("No data available")



print(prices)
