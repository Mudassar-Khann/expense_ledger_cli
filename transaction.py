from datetime import datetime, timezone


class Transaction:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now(timezone.utc).isoformat() if date is None else date

    def readable_date(self):
        dt = datetime.fromisoformat(self.date).astimezone()
        return dt.strftime("%d %b %Y, %I:%M %p")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    def __repr__(self):
        return f"Transaction({self.amount}, {self.category}, {self.description})"
