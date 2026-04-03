from datetime import datetime, timezone

class Transcation:

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now(timezone.utc).isoformat()


    def to_dict(self):
        return {
            "amount" : self.amount,
            "category" : self.category,
            "description" : self.description,
            "date" : self.date
        }


    def __repr__(self):
        return f"Transaction({self.amount}, {self.category}, {self.description}, {self.date})"








