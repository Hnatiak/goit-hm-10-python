from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        # Валідація формату номера телефону (10 цифр)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            self.phones.remove(phone_obj)

    # def edit_phone(self, old_phone, new_phone):
    #     old_phone_obj = Phone(old_phone)
    #     new_phone_obj = Phone(new_phone)

    #     if old_phone_obj in self.phones:
    #         self.remove_phone(old_phone)
    #         self.add_phone(new_phone)
    #     else:
    #         raise ValueError("Phone number does not exist")
    def edit_phone(self, old_phone, new_phone):
        old_phone_found = False
    
        for i, phone_obj in enumerate(self.phones):
            if phone_obj.value == old_phone:
                old_phone_found = True
                self.phones[i] = Phone(new_phone)  # Замінюємо старий номер новим
                break
            
        if not old_phone_found:
            raise ValueError("Phone number does not exist")

        # self.remove_phone(old_phone)
        # self.add_phone(new_phone)

    def find_phone(self, phone):
        phone_obj = Phone(phone)
        for p in self.phones:
            if p == phone_obj:
                return p.value
        return None

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


















# from collections import UserDict

# class Field:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name(Field):
#     pass

# class Phone(Field):
#     def __init__(self, value):
#         # Валідація формату номера телефону (10 цифр)
#         if not value.isdigit() or len(value) != 10:
#             raise ValueError("Invalid phone number format")
#         super().__init__(value)
        
#     def __eq__(self, other):
#         return self.value == other.value

# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []

#     def add_phone(self, phone):
#         self.phones.append(Phone(phone))

#     def remove_phone(self, phone):
#         phone_obj = Phone(phone)
#         if phone_obj in self.phones:
#             self.phones.remove(phone_obj)

#     def edit_phone(self, old_phone, new_phone):
#         old_phone_obj = Phone(old_phone)
#         new_phone_obj = Phone(new_phone)

#         if old_phone_obj not in self.phones:
#             raise ValueError("Phone number does not exist")

#         self.remove_phone(old_phone)
#         self.add_phone(new_phone)

#     def find_phone(self, phone):
#         phone_obj = Phone(phone)
#         for p in self.phones:
#             if p == phone_obj:
#                 return p.value
#         return None

#     def __str__(self):
#         phones_str = '; '.join(str(phone) for phone in self.phones)
#         return f"Contact name: {self.name.value}, phones: {phones_str}"

# class AddressBook(UserDict):
#     def add_record(self, record):
#         self.data[record.name.value] = record

#     def find(self, name):
#         return self.data.get(name)

#     def delete(self, name):
#         if name in self.data:
#             del self.data[name]





# # Створення нової адресної книги
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
