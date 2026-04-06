import json
import os

FILE = "data/transactions.json"


def save(transactions):
    os.makedirs("data", exist_ok=True)

    data = [t.to_dict() for t in transactions]
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
