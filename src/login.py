from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .utils.constants import LOGIN_URL
from .utils.credentials import ACCOUNT_ID, PASSWORD

def login(driver, account_id=ACCOUNT_ID, password=PASSWORD):
    try:
        driver.get(LOGIN_URL)

        # Wait for login fields
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        # Enter Account ID
        account_input = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        account_input.send_keys(account_id)

        # Enter Password
        password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        password_input.send_keys(password)

        # Click the Login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

    except Exception as e:
        print(f"Error during login: {e}")
        raise
