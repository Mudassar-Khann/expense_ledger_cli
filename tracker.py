from transaction import Transcation
import storage

class ExpenseTracker:

    def __init__(self):
        self.transictions = []

    def add_transiction(self, amount, category, description):

        self.transictions.append(Transcation(amount, category, description,))

        storage.save(self.transictions)




    def list_transactions(self):
        if  not self.transictions:
            yield False
        no = 0
        for i in self.transictions:
            no += 1
            yield f"[{no}] {i.amount} | {i.category} | {i.description} | {i.readable_date()}"


    def search_transactions(self, keyword=None, category=None):
        if keyword  and category:
            return [x for x in self.transictions if keyword in x.decription and category in x.category]

        elif keyword and not category:
             return [x for x in self.transictions if keyword in x.decription]

        elif category and not keyword:
             return [x for x in self.transictions if category in x.category]

        else:
            return self.transictions










