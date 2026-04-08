from tracker import ExpenseTracker

import sys

def test_add_transaction():

    tr = ExpenseTracker()

    tr.add_transaction("500", "food", "lunch")
    tr.add_transaction("500", "food", "burger")
    tr.add_transaction("500", "food", "pizza")

    assert len(tr.transactions) == 3


def test_search_transaction():

    tr = ExpenseTracker()

    tr.add_transaction("500", "food", "Burger")
    tr.add_transaction("500", "food", "pizza")
    tr.add_transaction("500", "food", "lunch")

    amount = tr.search_transactions(category="foo")
    result = tr.search_transactions(keyword="bur")

    assert len(amount) == 3

    assert result[0].description == "Burger"








