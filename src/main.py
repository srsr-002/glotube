from selenium import webdriver
import os
import scraping

def main():
    if "REMOTE_SELENIUM_URL" in os.environ:
        driver = webdriver.Remote(
            command_executor=os.environ["REMOTE_SELENIUM_URL"],
            options=webdriver.ChromeOptions()
        )
    else:
        driver = webdriver.Chrome()

    try:
        infoScrap = scraping.load_scraping_info("target.json")
        scraping.access_url(driver, infoScrap['url'])
        content = scraping.scrape_target(driver, infoScrap['selector'])
        print(content)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()