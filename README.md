# Coffee Web Scraper

This Python script demonstrates web scraping using Selenium and CSV handling. The script, named "Coffee Web Scraper," efficiently extracts product descriptions for a list of coffee-related items from a designated website. The collected data is then organized and saved in a CSV file for further analysis.

## Features:

- **Automation:** Utilizes Selenium for automated web browsing and data extraction.
- **Dynamic Searching:** Takes a list of coffee product titles and retrieves corresponding descriptions.
- **CSV Export:** Extracted data is neatly stored in a CSV file with customizable headers.
- **Efficiency:** Employs Undetected ChromeDriver to enhance scraping process by bypassing detection mechanisms.

## Usage:

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   Copy `.env.example` and rename it to `.env`:

   ```
   SEARCH_URL=<your_search_url>
   PRODUCTS_CSV=Coffee Scraper
   CSS_SELECTOR_PRODUCT=<css_selector_for_product_link>
   CSS_SELECTOR_DESCRIPTION=<css_selector_for_product_description>
   ```

3. **Run the Script:**

   ```bash
   py main.py
   ```

4. **Output:**
   Extracted data saved in `output.csv` with "product_title" and "product_description" headers.
