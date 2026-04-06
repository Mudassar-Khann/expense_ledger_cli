import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s"
)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)


def log_search(keyword, category, result):
    logging.info(f"Search: keyword={keyword or None} category={category or None} results={result}")






