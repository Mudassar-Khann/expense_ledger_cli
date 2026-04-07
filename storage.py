import json
import os
import sys

DATA_FILE = os.path.join("data", "transactions.json")


def save(transactions):
    os.makedirs("data", exist_ok=True)

    data = [t.to_dict() for t in transactions]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)




def clear_file():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

