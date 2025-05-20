from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

print("Starting driver...")
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

try:
    url = "https://owasp.org/www-project-top-ten/"
    print(f"Loading page: {url}")
    driver.get(url)

    items = driver.find_elements(By.XPATH, "//li[a/strong[contains(text(), '2021')]]")

    results = []

    for item in items:
        try:
            a_tag = item.find_element(By.TAG_NAME, "a")
            title = a_tag.text.strip()
            href = a_tag.get_attribute("href").strip()
            if title and href:
                results.append({"Title": title, "Link": href})
        except Exception as e:
            print("Skipping one item due to error:", type(e).__name__)

    print("Extracted OWASP Top 10 vulnerabilities:")
    for r in results:
        print(f"- {r['Title']} -> {r['Link']}")

    with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Link"])
        writer.writeheader()
        writer.writerows(results)

    print("Saved to owasp_top_10.csv")

except Exception as e:
    print("An error occurred:", type(e).__name__, e)

finally:
    driver.quit()
    print("Driver closed")
