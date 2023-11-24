from selenium.webdriver.common.by import By
import json

# ターゲット制御情報をロード(パターン)
def load_scraping_info(file_path):
    with open(file_path, 'r') as file:
        selectors = json.load(file)
    return selectors

# ターゲットのURLにアクセス
def access_url(driver, url):
    driver.get(url)

# ターゲットをスクレイピング
def scrape_target(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return element.text