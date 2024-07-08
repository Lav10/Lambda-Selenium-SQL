from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

# def lambda_handler(event, context):
if __name__=='__main__':
    # Get current working directory
    cwd = os.getcwd()

    # Set up Chrome options
    chrome_options = Options()
    prefs = {'download.default_directory': cwd}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # Needed for running headless on Windows
    chrome_options.add_argument('--window-size=1920,1200')  # Set window size to avoid issues in headless mode
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--remote-debugging-port=9230")

    if os.path.exists(os.path.join(cwd, 'annual-enterprise-survey-2023-financial-year-provisional.csv')):
        os.remove(os.path.join(cwd, 'annual-enterprise-survey-2023-financial-year-provisional.csv'))

    # Set up the Chrome driver (ensure you have the correct path to chromedriver)
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the website
    driver.get('https://www.stats.govt.nz/large-datasets/csv-files-for-download/')  

    href_value = '/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv'
    download_button = driver.find_element(By.XPATH, '/html/body/div[13]/div/div/div/main/section/div/div/div/article/div/div[2]/article/ul/li[1]/div/div/h3/a')
    download_button.click()

    time.sleep(3)
    # Close the browser after the download is complete (optional)
    driver.stop_client()
    driver.close()
    driver.quit()
