from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import csv
import json

# === CONFIGURE BROWSER ===
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
    # === BASIC SCRAPING ===
    print("Loading page")
    driver.get("https://en.wikipedia.org/wiki/Web_scraping")
    print("\nPage title:", driver.title)

    body = driver.find_element(By.CSS_SELECTOR, 'body')

    links = body.find_elements(By.CSS_SELECTOR, 'a')
    if links:
        print("\nFirst link href:", links[0].get_attribute('href'))

    main_div = body.find_element(By.CSS_SELECTOR, 'div[id="mw-content-text"]')
    if main_div:
        bolds = main_div.find_elements(By.CSS_SELECTOR, 'b')
        if bolds:
            print("\nFirst bold text:", bolds[0].text)

    image_entries = driver.find_elements(By.CSS_SELECTOR, 'img[src]')
    images = [img.get_attribute('src') for img in image_entries]
    print("\nNumber of images:", len(images))
    if images:
        print("\nFirst image src:", images[0])

    # === TARGETED XPATH SCRAPING ===
    print("\nExtracting 'See also' section links")

    see_also_links = []
    see_also_h2 = driver.find_element(By.CSS_SELECTOR, '[id="See_also"]')

    if see_also_h2:
        parent_div = see_also_h2.find_element(By.XPATH, '..')
        if parent_div:
            see_also_div = parent_div.find_element(By.XPATH, 'following-sibling::div')
            link_elements = see_also_div.find_elements(By.CSS_SELECTOR, 'a')
            for link in link_elements:
                name = link.text.strip()
                url = link.get_attribute("href")
                if name and url:
                    print(f"{name}: {url}")
                    see_also_links.append({"name": name, "url": url})

    # === ACCESSING ROBOTS.TXT ===
    print("\nAccessing robots.txt")
    robots_url = "https://en.wikipedia.org/robots.txt"
    driver.get(robots_url)
    robots_text = driver.page_source

    lines = robots_text.strip().split('\n')
    print("\nFirst 5 lines of robots.txt:")
    for line in lines[:5]:
        print(line)

    # === MANAGING REQUESTS AND HANDLING ERRORS ===
    print("\nTesting request handling with sleep and multiple pages")

    try:
        driver.get('https://example.com')
        print("Loaded example.com")

        sleep(2)

        driver.get('https://www.iana.org/domains/reserved')
        print("Loaded IANA reserved domains page")

        expected_title = "IANA — IANA-managed Reserved Domains"
        if driver.title != expected_title:
            print(f"Warning: Unexpected page title - got '{driver.title}'")

    except Exception as e:
        print(f"An exception occurred during multi-page scraping: {type(e).__name__} - {e}")

    # === SAVING SCRAPED DATA TO FILES ===
    print("\nSaving 'See also' links to CSV and JSON files")

    with open('see_also_links.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Link"])
        for link in see_also_links:
            writer.writerow([link["name"], link["url"]])
    print("Data saved to see_also_links.csv")

    with open('see_also_links.json', 'w', encoding='utf-8') as json_file:
        json.dump({"links": see_also_links}, json_file, indent=4)
    print("Data saved to see_also_links.json")

except Exception as e:
    print("Error occurred")
    print(f"\nException: {type(e).__name__} - {e}")

finally:
    driver.quit()
    print("Driver closed")
