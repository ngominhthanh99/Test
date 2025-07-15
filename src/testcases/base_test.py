import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.configreader import configreader

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(configreader.get_base_url())
        request.cls.driver = driver
        yield  
        driver.quit()

        

        