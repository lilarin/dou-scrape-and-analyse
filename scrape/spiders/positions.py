import csv
from pathlib import Path
from typing import Generator
from urllib.parse import urljoin
import time
import scrapy
from scrapy.http import Response
from scrape.config import (
    experiences,
    scrape_url,
    scrape_position,
    save_dir
)


class PositionsSpider(scrapy.Spider):
    name = "positions"
    allowed_domains = ["jobs.dou.ua"]

    dir = Path(save_dir)
    dir.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%d-%m-%Y")

    filepath = dir / f"{name}_{scrape_position}_{timestamp}.csv"

    def start_requests(self) -> Generator:
        with open(self.filepath, mode="a", newline="", encoding="utf-8") as file:
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

        for experience, experience_filter in experiences.items():
            url = urljoin(
                scrape_url,
                "?category=" + scrape_position + experience_filter
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
