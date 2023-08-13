from dotenv import load_dotenv
import os
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By

load_dotenv()
SEARCH_URL = os.getenv("SEARCH_URL")
PRODUCTS_CSV = os.getenv("PRODUCTS_CSV")


def main():
    driver = Chrome()
    products = [
        product.strip().replace(" ", "+") for product in PRODUCTS_CSV.split(",")
    ]

    driver.get(f"{SEARCH_URL}?search={products[0]}")

    product_result = driver.find_element(By.CSS_SELECTOR, "li.item.result")
    product_result.click()

    product_description = driver.find_element(
        By.CSS_SELECTOR, "div.product-description p:first-of-type"
    ).text

    print(product_description)

    input()
    driver.close()


if __name__ == "__main__":
    main()
