from selenium import webdriver
import scraping

def main():
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