from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .basepages import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.enter_text(self.username_field, username)

    def enter_password(self, password):
        self.enter_text(self.password_field, password)

    def click_login(self):
        self.click(self.login_button)     

    def login(self,username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

