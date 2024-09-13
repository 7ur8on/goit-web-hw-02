from abc import ABC, abstractmethod


class UserInterface(ABC):

    @abstractmethod
    def parse_input(self, user_input):
        pass

    @abstractmethod
    def add_contact(self, args, book):
        pass

    @abstractmethod
    def change_contact(self, args, book):
        pass

    @abstractmethod
    def show_phone(self, args, book):
        pass

    @abstractmethod
    def add_birthday(self, args, book):
        pass

    @abstractmethod
    def show_birthday(self, args, book):
        pass

    @abstractmethod
    def del_record(self, args, book):
        pass

    @abstractmethod
    def save_data(self, book, filename="addressbook.pkl"):
        pass

    @abstractmethod
    def load_data(self, filename="addressbook.pkl"):
        pass
