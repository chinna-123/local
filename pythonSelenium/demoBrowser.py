import time

from selenium import webdriver

from selenium.webdriver.common.service import Service

# Our selenium webdriver will not directly invoke with chrome browser in b/w we have a chrome driver service
# Chrome driver service plays a vital role in invoking the chrome browser
# chrome browser will not direct permission to any automation tools like  selenium webdriver to invoke and to perform actions

# service_obj = Service('') # provide path of the chrome driver
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://rahulshettyacademy.com/')
print(driver.title)
print(driver.current_url)
time.sleep(2)
