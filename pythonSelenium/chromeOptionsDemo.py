import time

from selenium import webdriver

# Headless Browser   Head Mode--> Browser Invoking

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")

chrome_options.add_argument("--ignore-certificate-errors")

d = webdriver.Chrome(options=chrome_options)
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/angularpractice/")
print(d.title)