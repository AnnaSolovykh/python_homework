# TASKS 3, 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

print("Starting driver")
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

try:
    url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    print("Loading page")
    driver.get(url)

    items = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
    print(f"Number of results found: {len(items)}")

    results = []

    for item in items:
        try:
            title_element = item.find_element(By.CSS_SELECTOR, 'h2.cp-title a')
            title = title_element.text.strip()
        except:
            title = ""

        try:
            author_elements = item.find_elements(By.CSS_SELECTOR, 'a.author-link')
            authors = "; ".join([a.text.strip() for a in author_elements])
        except:
            authors = ""

        try:
            format_element = item.find_element(By.CSS_SELECTOR, 'div.cp-format-info span.display-info-primary')
            format_year = format_element.text.strip()
        except:
            format_year = ""

        book = {
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        }
        results.append(book)

    df = pd.DataFrame(results)
    print(df)

    df.to_csv("get_books.csv", index=False)
    with open("get_books.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)


except Exception as e:
    print("An error occurred:", type(e).__name__, e)

finally:
    driver.quit()
    print("Driver closed")
