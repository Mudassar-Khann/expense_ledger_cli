from transaction import Transaction
import storage

class ExpenseTracker:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description):

        self.transactions.append(Transaction(amount, category, description,))

        storage.save(self.transactions)




    def list_transactions(self):
        result = []
        for i, t in enumerate(self.transactions, 1):
            result.append(f"[{i}] {t.amount} | {t.category} | {t.description} | {t.readable_date()}")
        return result

    def search_transactions(self, keyword=None, category=None):

        results = []

        for t in self.transactions:
            if keyword and keyword not in t.description.lower():
                continue

            if category and category not in t.category.lower():
                continue

            results.append(t)

        return results

    def load_transactions(self):
        for t in storage.load():
            self.transactions.append(
                Transaction(t["amount"], t["category"], t["description"], t["date"])
            )











