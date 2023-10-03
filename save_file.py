from Person import *
def save_person(person:Person):

    try:
        file_person = open(f"{person.surname}.txt", 'a')
        try:
            file_person.write(person.__str__())
        except Exception as e:
            print(e)
        finally:
            file_person.close()
    except Exception as ex:
        print(ex)