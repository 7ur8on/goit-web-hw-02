from userview import UserInterface
from decorator import input_error
from addressbook import AddressBook
from record import Record
import pickle


class ConsoleView(UserInterface):

    @input_error
    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    @input_error
    def add_contact(self, args, book: AddressBook):
        name, phone, *_ = args
        record = book.find_record(name)
        if phone.isdigit() and len(phone) != 10:
            return "The phone must have 10 digits"
        if record is None:
            record = Record(name)
            book.add_record(record)
            if phone.isdigit() and len(phone) == 10:
                record.add_phone(phone)
                return "Contact added."
        else:
            if phone.isdigit() and len(phone) == 10:
                record.add_phone(phone)
                return "Contact updated."

    @input_error
    def change_contact(self, args, book: AddressBook):
        name, old_phone, new_phone, *_ = args
        record = book.find_record(name)
        record.edit_phone(old_phone, new_phone)
        return f"Contact {name} updated with number {new_phone}."

    @input_error
    def show_phone(self, args, book: AddressBook):
        name, *_ = args
        record = book.find_record(name)
        return record.show_phones()

    @input_error
    def add_birthday(self, args, book: AddressBook):
        name, birthday, *_ = args
        record = book.find_record(name)
        if record is None:
            return f"Name {name} does not exist"
        if record.birthday is not None:
            return f"Name {name} with birthday {record.birthday} is exist"
        record.add_birthday_in_class(birthday)
        return f"Birthday for {name} added"

    @input_error
    def show_birthday(self, args, book: AddressBook):
        name, *_ = args
        record = book.find_record(name)
        return record.birthday.value

    @input_error
    def del_record(self, args, book: AddressBook):
        name, *_ = args
        if book.find_record(name) is None:
            return f"Record with {name} not found."
        else:
            book.delete_record(name)
            return f"Record with name {name} is deleted"

    def save_data(self, book, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    def load_data(self, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()
