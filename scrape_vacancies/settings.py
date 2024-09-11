BOT_NAME = "scrape_vacancies"

SPIDER_MODULES = ["scrape_vacancies.spiders"]
NEWSPIDER_MODULE = "scrape_vacancies.spiders"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
   "scrape_vacancies.middlewares.SeleniumMiddleware": 543,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
