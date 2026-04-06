from transaction import Transcation
import storage

class ExpenseTracker:

    def __init__(self):
        self.transictions = []

    def add_transiction(self, amount, category, description):

        self.transictions.append(Transcation(amount, category, description,))

        storage.save(self.transictions)




    def list_transactions(self):
        result = []
        for i, t in enumerate(self.transactions, 1):
            result.append(f"[{i}] {t.amount} | {t.category} | {t.description} | {t.readable_date()}")
        return result

    def search_transactions(self, keyword=None, category=None):
        if keyword  and category:
            return [x for x in self.transictions if keyword in x.desription and category in x.category]

        elif keyword and not category:
             return [x for x in self.transictions if keyword in x.desription]

        elif category and not keyword:
             return [x for x in self.transictions if category in x.category]

        else:
            return self.transictions

    def load_transactions(self):
        for trans in storage.load():
            self.transictions.append(Transcation(trans["amount"], trans["category"], trans["description"], trans["date"]))











