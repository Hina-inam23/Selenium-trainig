from selenium import webdriver
import HtmlTestRunner
import unittest
from selenium.webdriver.common.keys import Keys
import time

class Login(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://www.gmail.com/")


    def test_Login(self):
        username = self.browser.find_element_by_id("identifierId")
        username.send_keys("hina.inam@tkxel.com")
        login_attempt = self.browser.find_element_by_class_name('CwaK9').click()
        time.sleep(5)
        password = self.browser.find_element_by_class_name("whsOnd.zHQkBf")
        password.send_keys("!tkxel23!")
        login_attempt =self.browser.find_element_by_class_name("CwaK9").click()


    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))
    HtmlTestRunner.main()