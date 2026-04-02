import tracker




def main():
    commands = {"add", "list", "search", "exit"}

    print("Available commands:" , commands)
    while True:


        user_choice = input("Enter your command: ").strip().lower()

        if user_choice not in commands:
            print(user_choice, "command is not avelibal")
            continue

        if user_choice == "add":
            pass
        elif user_choice == "list":
            pass
        elif user_choice == "search":
            pass

        elif user_choice == "exit":
            break






if __name__ == "__main__":

   main()






