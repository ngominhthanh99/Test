import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        path = "D:/tools/chromedriver.exe"
        service = Service(path) if os.path.exists(path) else Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
        self.driver.set_page_load_timeout(15) 
        print(f"The web's url is: {self.driver.current_url}")
        request.cls.driver=self.driver
        yield
        self.driver.quit()

        


        