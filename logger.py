import logging, os

os.makedirs("logs", exist_ok=True)


def log_info(messsage, amount=None,  category=None, description=None, result=None):
    logging.basicConfig(filename="logs/app.log", level=logging.INFO,
    format=f"[%(levelname)s] {messsage} Added Transaction {amount} {category} {description}")

def log_error(input):
    logging.basicConfig(filename="logs/app.log", level=logging.ERROR,
    format=f"[%(asctime)s] [%(levelname)s] Invalid amount input: {input}")










