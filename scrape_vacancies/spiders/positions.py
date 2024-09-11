import csv
from typing import Generator
from urllib.parse import urljoin
import time

import scrapy
from scrapy.http import Response
from scrape_vacancies.config import (
    experience_levels,
    scrape_url
)

from app.config import domain


class PositionsSpider(scrapy.Spider):
    name = "positions"
    allowed_domains = ["jobs.dou.ua"]

    filepath = f"scrapped_data/{domain}_{time.strftime("%d-%m-%Y")}.csv"

    def start_requests(self) -> Generator:
        with open(self.filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Position",
                    "Experience",
                    "Company",
                    "Location",
                    "Date",
                    "Details"
                ]
            )

        for experience, experience_filter in experience_levels.items():
            url = urljoin(
                scrape_url,
                "?category=" + domain + experience_filter
            )
            request = scrapy.Request(url=url, callback=self.parse)
            request.meta["experience"] = experience
            yield request

    def parse(self, response: Response, **kwargs) -> Generator | None:
        job_offers = response.css(".l-vacancy")

        if job_offers:
            for offer in job_offers:
                position = offer.css(".vt::text").get()
                company = offer.css(".company::text").get()
                locations = offer.css(".cities::text").get()
                date = offer.css(".date::text").get()

                offer_detail_link = offer.css(".vt::attr(href)").get()

                detail_url = urljoin(
                    response.url, offer_detail_link
                )
                request = scrapy.Request(
                    url=detail_url, callback=self.parse_details
                )
                request.meta["position"] = position
                request.meta["experience"] = response.meta["experience"]
                request.meta["company"] = company.replace(" ", "")
                request.meta["locations"] = locations
                request.meta["date"] = date
                request.meta["use_selenium"] = False
                yield request

    def parse_details(self, response: Response) -> None:
        position = response.meta["position"]
        experience = response.meta["experience"]
        company = response.meta["company"]
        locations = response.meta["locations"]
        date = response.meta["date"]

        details = response.css(".b-typo.vacancy-section ::text").getall()
        details = " ".join(details).strip()
        details_text = details.replace(" ", " ")

        with open(self.filepath, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    position,
                    experience,
                    company,
                    locations,
                    date,
                    details_text
                ]
            )
