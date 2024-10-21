import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(d)
# action.click_and_hold()  # long press
# action.double_click()
# action.drag_and_drop()
# action.move_to_element() # shift the mouse pointer to the selected element
action.move_to_element(d.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
# action.context_click(d.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(d.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(3)