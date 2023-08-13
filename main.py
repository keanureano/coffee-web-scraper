from dotenv import load_dotenv
import os
from undetected_chromedriver import Chrome

load_dotenv()
WEBSITE_URL = os.getenv("WEBSITE_URL")


def main():
    driver = Chrome()
    driver.get(WEBSITE_URL)

    input("Press Enter to Close")
    driver.close()


if __name__ == "__main__":
    main()
