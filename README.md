# Job Scraper for dou.ua

This tool scrapes and analysis vacancies from the [dou.ua](https://jobs.dou.ua/vacancies) website, allowing users to specify  domains and technologies to collect the desired information.

## Features

- Scrape job positions using the Scrapy and Selenium frameworks.
- Specify domains for search (e.g., Python, Java, QA, etc.).
- Filter jobs based on technologies to gauge their popularity.
- Export analysed in Jupiter Notebook charts to a PDF file for easy sharing and review.
- Support for manual and automated execution via the `main.py` script, or manual launch with Scrapy and Jupyter Notebook.

## Configuration

You can modify the scraping configuration in the `app.config` section to specify domain and technologies to scrap.

## Launch

You can run the project using the `main.py` script located in the `app` directory:

```bash
python app/main.py
```
Alternatively, you can manually scrape data using:
```bash
scrapy crawl vacancies
```
To launch the Jupyter Notebook manually, run it yourself as needed.

## Requirements

- Python 3.10+
- Scrapy
- Selenium
- Jupyter Notebook

You can install all dependencies by running:
```bash
pip install -r requirements.txt
```

##
