import os
import subprocess
import time
import papermill as pm

from config import domain


def run_scrapy_crawler():
    subprocess.run(["scrapy", "crawl", "vacancies"])


def run_notebook():
    notebook_path = "data_analysis/notebook.ipynb"
    processed_notebook_path = "data_analysis/processed.ipynb"
    csv_file_name= f"{domain}_{time.strftime("%d-%m-%Y")}.csv"
    pm.execute_notebook(
        notebook_path,
        processed_notebook_path,
        parameters=dict(file_name=csv_file_name)
    )
    os.remove(processed_notebook_path)


if __name__ == "__main__":
    run_scrapy_crawler()
    run_notebook()
