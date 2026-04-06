import json




def save(transactions: list):

    data = [i.to_dict() for i in transactions ]
    with open("data/transactions.json", "w", encoding="utf-8") as f:
          json.dump(data, f, indent=5)





def load():
     with open("data/transactions.json", "r", encoding="utf-8") as f:
         data = json.load(f)
         return data






