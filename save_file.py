from Person import *
def save_person(person:Person):

    try:
        file_person = open(f"info_persons/{person.surname}.txt", 'a', encoding="UTF-8")
        try:
            file_person.write(person.__str__())
        except Exception as e:
            print(e)
        finally:
            file_person.close()
    except Exception as ex:
        print(ex)