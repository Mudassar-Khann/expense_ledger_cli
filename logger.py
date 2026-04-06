import logging, os

os.makedirs("logs", exist_ok=True)


def log_info(input):
    logging.basicConfig(filename="logs/app.log", level=logging.INFO
    format=f"[%(levelname)s]" {input})









