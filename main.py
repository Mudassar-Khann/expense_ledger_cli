from tracker import ExpenseTracker
from logger import log_error, log_info, log_search


def main():
    tr = ExpenseTracker()
    tr.load_transactions()

    commands = {"add", "list", "search", "exit"}
    print("Available commands:" , commands, "\n")

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

            # basic validation
            if not amount.isdigit():
                print("Invalid amount.")
                log_error(f"Invalid amount input: {amount}")
                continue

            tr.add_transaction(amount, category, description)
            log_info(f"Added transaction: {amount} {category} {description}")

            print("Transaction added successfully.\n")


        elif user_choice == "list":

            transanction_list = tr.list_transactions()

            if not next(transanction_list):
                print("List is empty \n")
                continue
            print("Press 'Enter' to look one at a time or type 'all' to see full list ")
            option = input(">")
            if option == "all":
                 for tras in transanction_list:
                    print(tras)

            elif not option:
                print("press enter to go trough list ")
                for tras in transanction_list:
                    option = input("")
                    print( tras)


            else:
                print("wrong input if you wanna search an item write search ")
                continue

            print("End of transactions ", end="\n\n")


        elif user_choice == "search":
            print("Enter 'Keyword' or 'Category' of what you wanna search or press 'Enter' to skip ")
            keyword = input("Enter the keyword: ").strip().lower()
            category = input("Enter the category: ").strip().lower()


            search_result = tr.search_transactions(keyword, category)

            log_search(keyword, category, len(search_result))

            if search_result:

                no = 0
                for trans in search_result:
                    no += 1
                    print(f"{no}. Amount: {trans.amount} | Category: {trans.category} | Description: {trans.description}")

            else:
                print(search_result)
                print("No transactions found.")

            print("\n")

        elif user_choice == "exit":
            break






if __name__ == "__main__":

   main()








