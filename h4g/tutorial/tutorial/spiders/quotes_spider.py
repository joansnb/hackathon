import chromedriver_binary
import scrapy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger
class CountriesSpiderSpider(scrapy.Spider):
    # Initializing log file
    logfile("openaq_spider.log", maxBytes=1e6, backupCount=3)
    name = "countries_spider"
    allowed_domains = ["toscrape.com"]
#0 x Using a dummy website to start scrapy request
    def start_requests(self):
        url = "https://www.google.com/search?q=joan+navarrete"
        yield scrapy.Request(url=url, callback=self.parse_countries)

    def parse_countries(self, response):
# driver = webdriver.Chrome()  # To open a new browser window and navigate it
# Use headless option to not open a new browser window
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(ChromeDriverManager().install())

        #driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
# Getting list of Countries
        driver.get("https://www.google.com/search?q=joan+navarrete")
# Implicit wait
        driver.implicitly_wait(2000)
# Explicit wait
        wait = WebDriverWait(driver, 5)
        print("AAAA")
        q = driver.find_element(By.CSS_SELECTOR, 'div.quote')
        print(q.get_attribute('innerHTML'))

       # quotes = driver.find_elements_by_class_name("quote")
# Using Scrapy's yield to store output instead of explicitly writing to a JSON file
        #for country in countries:
            #print(country)

        #driver.quit()