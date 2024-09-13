from consolview import ConsoleView


def main():
    view = ConsoleView()
    book = view.load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = view.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            view.save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(view.add_contact(args, book))

        elif command == "change":
            print(view.change_contact(args, book))

        elif command == "phone":
            print(view.show_phone(args, book))

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            print(view.add_birthday(args, book))

        elif command == "show-birthday":
            print(view.show_birthday(args, book))

        elif command == "birthdays":
            print(book.get_upcoming_birthdays())

        elif command == "delete-record":
            print(view.del_record(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
