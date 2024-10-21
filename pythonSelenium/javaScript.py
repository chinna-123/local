import time

from selenium import webdriver

# Headless Browser

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-errors")

d = webdriver.Chrome(options=chrome_options)
d.maximize_window()
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
d.execute_script("window.scrollBy(0,document.body.scrollHeight)")
d.get_screenshot_as_file("screen.png")
time.sleep(3)