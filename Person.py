class Person:
    def __init__(self, surname, name, patronymic, phone_number, date_of_birth, gender):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.gender = gender
    
    def __str__(self) -> str:
        return f"<{self.surname}><{self.name}><{self.patronymic}><{self.phone_number}><{self.date_of_birth}><{self.gender}>"