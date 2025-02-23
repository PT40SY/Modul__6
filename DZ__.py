from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        self.value = None
        self.set_value(value)

    def set_value(self, value):
        if self.is_valid_phone(value):
            self.value = value
        else:
            raise ValueError(f"Invalid phone number: {value}")

    def is_valid_phone(self, value):
        return re.fullmatch(r'\d{10}', value) is not None

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError(f"Phone {phone} not found in record.")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.set_value(new_phone)
                return
        raise ValueError(f"Phone {old_phone} not found in record.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Contact with name {name} not found.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john) 

found_phone = john.find_phone("5555555555")
print(f"{john.name.value}: {found_phone}") 

book.delete("Jane")
