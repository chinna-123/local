import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.get("https://rahulshettyacademy.com/dropdownsPractise/")

d.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = d.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(2)

'''
we can retrieve the text from webpage by using (text)
if the text is already present on the webpage when we load the page

if we retrieve the text that is not present in the web page at the time
of loading the page    then we have to use get_attribute("value") method

when you update the value dynamically through script how do you extract the text
  
'''
# print(d.find_element(By.ID, "autosuggest").text)
print(d.find_element(By.ID, "autosuggest").get_attribute("value"))
assert d.find_element(By.ID, "autosuggest").get_attribute("value") == "India"