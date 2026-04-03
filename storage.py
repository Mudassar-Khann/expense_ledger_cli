import json



def save(transactions: list):

    data = [i.to_dict() for i in transactions ]
    with open("data/transactions.json", "w", encoding="utf-8") as f:
          json.dump(data, f, indent=5)





