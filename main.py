from dotenv import load_dotenv
import os
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By

load_dotenv()
SEARCH_URL = os.getenv("SEARCH_URL")
PRODUCTS_CSV = os.getenv("PRODUCTS_CSV")


def main():
    driver = Chrome()
    product_titles = [
        product.strip().replace(" ", "+") for product in PRODUCTS_CSV.split(",")
    ]

    product_data = []

    for product_title in product_titles:
        driver.get(f"{SEARCH_URL}?search={product_title}")

        product_result = driver.find_element(By.CSS_SELECTOR, "li.item.result")
        product_result.click()

        product_description = driver.find_element(
            By.CSS_SELECTOR, "div.product-description p:first-of-type"
        ).text
        product_data.append((product_title, product_description))

    print(product_data)
    driver.close()


if __name__ == "__main__":
    main()
