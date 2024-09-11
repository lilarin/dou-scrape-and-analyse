# Job Scraper for dou.ua

This tool scrapes vacancies from the [dou.ua](https://jobs.dou.ua/vacancies) website, allowing users to specify domains and technologies for a more tailored job search. The scraped data is exported as plots into a PDF file for further analysis.

## Features

- Scrape job positions using the Scrapy and Selenium frameworks.
- Specify domains for search (e.g., Python, Java, QA, etc.).
- Filter jobs based on technologies to gauge their popularity.
- Export analysed in Jupiter Notebook charts to a PDF file for easy sharing and review.
- Support for manual and automated execution via the `main.py` script, or manual launch with Scrapy and Jupyter Notebook.

## Configuration

You can modify the scraping configuration in the `app.config` section.

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

## Dependencies

- Python 3.10 +
- Scrapy
- Selenium
- Jupyter notebook

You can install all dependencies by running:
```bash
pip install -r requirements.txt
```
