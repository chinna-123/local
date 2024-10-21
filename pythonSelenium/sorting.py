from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browserSortedVeggies = []
d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
d.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all vegetable names and store in list --> Browser
veggieWebElements = d.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

browserSortedVeggies.sort()

assert originalBrowserSortedList == browserSortedVeggies


