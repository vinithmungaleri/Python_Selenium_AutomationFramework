from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# service_obj = Service("/Users/rahulshetty/documents/chromedriver")

#-- Chrome
# driver = webdriver.Chrome(service=service_obj)

# -- Firefox
# driver = webdriver.Firefox(service=service_obj)

#-- Edge
# driver = webdriver.Edge(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
title = driver.title  # this is a property. no () needed.
curr_url = driver.current_url
print("URL: {} and Title: {}".format(curr_url, title))

driver.minimize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()  # methods need to be closed with ()
