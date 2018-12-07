from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://gmail.com")
time.sleep(10)
username = browser.find_element_by_id("identifierId")
username.send_keys("hina.inam@tkxel.com")
login_attempt = browser.find_element_by_class_name('CwaK9').click()
time.sleep(5)
password = browser.find_element_by_class_name("whsOnd.zHQkBf")
password.send_keys("!tkxel23!")
login_attempt = browser.find_element_by_class_name("CwaK9").click()
time.sleep(10);
browser.close()