from testcases.web_driver import BaseTest
from pages.loginpage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.configreader import configreader
from time import sleep

class TestLoginWeb(BaseTest):
    def test_login_valid(self):
        login_pg = LoginPage(self.driver)
        login_pg.do_login(configreader.get_username(), configreader.get_password())
        sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
        )
        
        print("\n Login successful!")

