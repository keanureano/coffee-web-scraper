from dotenv import load_dotenv
import os
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By

load_dotenv()
WEBSITE_URL = os.getenv("WEBSITE_URL")


def main():
    driver = Chrome()
    driver.get(WEBSITE_URL)

    search_icon = driver.find_element(By.CLASS_NAME, "desktop-search-icon")
    search_icon.click()

    input("Press Enter to Close")
    driver.close()


if __name__ == "__main__":
    main()
