from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumMiddleware:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def process_request(self, request, spider):
        if request.meta.get("use_selenium", True):
            self.driver.get(request.url)
            wait = WebDriverWait(self.driver, 1)

            while True:
                try:
                    load_more_button = wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".more-btn a"))
                    )
                    load_more_button.click()
                    time.sleep(1)
                except (NoSuchElementException, TimeoutException):
                    break

            body = self.driver.page_source
            return HtmlResponse(
                self.driver.current_url,
                body=body, encoding="utf-8", request=request
            )

    def __del__(self):
        self.driver.quit()
