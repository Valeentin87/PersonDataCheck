''' Напишите приложение, которое будет запрашивать у пользователя следующие данные в произвольном порядке, разделенные пробелом:
Фамилия Имя Отчество датарождения номертелефона пол

Форматы данных:
фамилия, имя, отчество - строки
датарождения - строка формата dd.mm.yyyy
номертелефона - целое беззнаковое число без форматирования
пол - символ латиницей f или m.'''
from check_data import *
from Person import *

def check_data_of_person():
    flag = True
    while flag:
        try:
            #person_data = input('введите через пробел следующие данные о себе: Фамилия Имя Отчество датарождения номертелефона пол и нажмите Enter: ')
            person_data = "Алла Пецина Александровна 8913184051  f 23.07.2012 "
            if person_data == "":
                raise Exception("вы не ввели данные!!! Попробуйте снова!!!")
            person_data_list = person_data.split()
            #print(person_data_list)
            
            if len(person_data_list)>6:
                raise Exception("вы ввели данных больше, чем требуется: проверьте и введите заново: ")
            elif len(person_data_list)<6:
                raise Exception("вы ввели данных меньше, чем требуется: проверьте и введите заново: ")
            elif check_date_of_birth(person_data_list)[1] == False:
                raise Exception("Во входных данных не корректная дата рождения!!!")
            elif check_gender(person_data_list)[1] == False:
                raise Exception("Во входных данных не корректный пол")
            elif check_patronymic(person_data_list, check_gender(person_data_list)[0])[1] == False:
                print(check_gender(person_data_list)[0])
                raise Exception("Во входных данных не корректное отчество")
            elif check_phone_number(person_data_list)[1] == False:
                raise Exception("Во входных данных не корректный номер телефона")
            elif check_surname(person_data_list, check_gender(person_data_list)[0])[1] == False:
                raise Exception("Во вхожных данных не корректная фамилия!!! ")
            
            else: 
                print("Вы ввели корректные данные, спасибо!!!")

                name_person = check_name(person_data_list.copy(), check_phone_number(person_data_list),check_date_of_birth(person_data_list), \
                    check_gender(person_data_list), check_surname(person_data_list, check_gender(person_data_list)[0]), check_patronymic(person_data_list, check_gender(person_data_list)[0]))
                
                return  Person(check_surname(person_data_list,check_gender(person_data_list)[0])[0],name_person[0],check_patronymic(person_data_list, check_gender(person_data_list)[0])[0],check_phone_number(person_data_list)[0], \
                        check_date_of_birth(person_data_list)[0],check_gender(person_data_list)[0]) 
                print(firt_Person)
                flag = False
            
            
        except Exception as e:
            print(e)

check_data_of_person()    









