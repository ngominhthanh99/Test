from src.utils.web_driver import setup_driver
from src.login import login
import time

def main():
    driver = setup_driver()
    
    try:
        # Log in
        login(driver)
        time.sleep(1)

    except Exception as e:
        print(f"Unexpected error in main execution: {e}")

    input()
    driver.quit()

if __name__ == "__main__":
    main()