from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)   #--> each action object needs to be ended with .perform() to perform that action.
#action.double_click(driver.find_element(By.))
#action.context_click()  # --> does right click action
#action.drag_and_drop()  #--> give start and target web elements path.
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()   #--> performs mouse hover.
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
