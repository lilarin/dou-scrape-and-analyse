# Vacancies Scraper for dou.ua

This tool scrapes and analysis vacancies and technologies trends from the [dou.ua](https://jobs.dou.ua/vacancies), allowing users to specify  domains and technologies to collect the desired information.

## Features

- Scrape vacancies using the Scrapy and Selenium frameworks.
- Specify domains for search (e.g., Python, Java, QA, etc.).
- Specify technologies to measure their popularity.
- Use Jupyter Notebook to analyze data and generate charts in a PDF file.
- Support automated execution via script, as well as manual launch with Scrapy and Jupyter Notebook.

## Examples

![image](https://imgur.com/50mzKpm.png)
![image](https://imgur.com/qtG2boe.png)
![image](https://imgur.com/pPHhrxo.png)


## Configuration

You can modify the scraping configuration in the `app.config` section to specify the domain and technologies to scrape.

## Launch

After filling out the `app.config` file, you can run the automated script using:

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
