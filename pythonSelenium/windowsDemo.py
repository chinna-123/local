from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.maximize_window()
d.delete_all_cookies()
d.implicitly_wait(5)

d.get("https://the-internet.herokuapp.com/windows")
d.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = d.window_handles
d.switch_to.window(windowsOpened[1])
print(d.find_element(By.TAG_NAME, "h3").text)
d.close()

d.switch_to.window(windowsOpened[0])
assert "Opening a new window" == d.find_element(By.TAG_NAME, "h3").text