import csv
from dotenv import load_dotenv
import os
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
SEARCH_URL = os.getenv("SEARCH_URL")
PRODUCTS_CSV = os.getenv("PRODUCTS_CSV")

CSS_SELECTOR_PRODUCT = os.getenv("CSS_SELECTOR_PRODUCT")
CSS_SELECTOR_DESCRIPTION = os.getenv("CSS_SELECTOR_DESCRIPTION")

OUTPUT_CSV_FILENAME = "output.csv"
CSV_HEADER = ["product_title", "product_description"]


def main():
    driver = initialize_driver()
    product_titles = get_product_titles()

    product_data = []

    for product_title in product_titles:
        product_data.append(scrape_product_data(driver, product_title))

    write_to_csv(OUTPUT_CSV_FILENAME, product_data)

    driver.close()


def initialize_driver():
    return Chrome()


def get_product_titles():
    return [product.strip() for product in PRODUCTS_CSV.split(",")]


def scrape_product_data(driver, product_title):
    driver.get(f"{SEARCH_URL}?search={product_title.replace(' ', '+')}")

    product_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR_PRODUCT))
    )
    product_result.click()

    product_description = (
        WebDriverWait(driver, 10)
        .until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, CSS_SELECTOR_DESCRIPTION)
            )
        )
        .text
    )

    return (product_title, product_description)


def write_to_csv(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(CSV_HEADER)
        csv_writer.writerows(data)


if __name__ == "__main__":
    main()
