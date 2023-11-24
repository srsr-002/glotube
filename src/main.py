from selenium import webdriver
import os
import scraping

def main():
    driver = webdriver.Remote(
        command_executor = os.environ["SELENIUM_URL"],
        options = webdriver.ChromeOptions()
    )

    try:
        infoScrap = scraping.load_scraping_info("target.json")
        scraping.access_url(driver, infoScrap['url'])
        content = scraping.scrape_target(driver, infoScrap['selector'])
        print(content)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()