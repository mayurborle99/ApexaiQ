"""Dot net Scrapper"""

#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()

#chrome instance
driver.get("https://dotnet.microsoft.com/en-us/download/dotnet/8.0")
time.sleep(1)

# Find all tables on the page
tables = driver.find_elements(By.TAG_NAME, "table")

# Loop through each table and scrape data
for index, table in enumerate(tables):
    # Extract table headers
    try:
        headers = [th.text.strip() for th in table.find_elements(By.XPATH, ".//thead/tr/th")]
    except:
        headers = []

    # Extract table rows
    table_data = []
    rows = table.find_elements(By.XPATH, ".//tbody/tr")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        col_data = [col.text.strip() for col in cols]
        if col_data:
            table_data.append(col_data)

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(table_data, columns=headers if headers else None)
    csv_filename = f"dotnet_table_{index+1}.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Saved: {csv_filename}")

# Close the browser
driver.quit()