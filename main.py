from tracker import ExpenseTracker
from logger import log_info, log_error, log_search

def main():
    tr = ExpenseTracker()
    tr.load_transactions()

    commands = {"add", "list", "search", "exit"}
    print("Available commands:", commands, "\n")

    while True:
        user_choice = input("Enter your command: ").strip().lower()

        if user_choice not in commands:
            print(user_choice, "command is not available")
            log_error(f"Invalid command: {user_choice}")
            continue

        if user_choice == "add":
            amount = input("Enter amount: ").strip()
            category = input("Enter category: ").strip().lower()
            description = input("Enter description: ").strip().lower()



            if not amount.isdigit():
                print("Invalid amount.")
                log_error(f"Invalid amount input: {amount}")
                continue

            tr.add_transaction(amount, category, description)
            log_info(f"Added transaction: {amount} {category} {description}")

            print("Transaction added successfully.\n")

        elif user_choice == "list":
            transactions = tr.list_transactions()

            if not transactions:
                print("List is empty\n")
                continue

            print("Press 'Enter' for one-by-one or type 'all'")
            option = input(">")

            if option == "all":
                for t in transactions:
                    print(t)

            elif not option:
                for t in transactions:
                    input()
                    print(t)

            else:
                print("Invalid option")
                continue

            print("End of transactions\n")

        elif user_choice == "search":
            keyword = input("Enter keyword: ").strip().lower()
            category = input("Enter category: ").strip().lower()

            results = tr.search_transactions(keyword, category)

            log_search(keyword, category, len(results))

            if results:
                for i, t in enumerate(results, 1):
                    print(f"{i}. Amount: {t.amount} | Category: {t.category} | Description: {t.description}")
            else:
                print("No transactions found.")

            print()

        elif user_choice == "exit":
            break





if __name__ == "__main__":
    main()
