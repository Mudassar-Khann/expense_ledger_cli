from transaction import Transcation
import storage

class ExpenseTracker:

    def __init__(self):
        self.transictions = []

    def add_transiction(self, amount, category, description):

        self.transictions.append(Transcation(amount, category, description,))

        storage.save(self.transictions)




    def list_transactions(self):
        pass

    def search_transactions(self, word):
        pass







