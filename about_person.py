''' Напишите приложение, которое будет запрашивать у пользователя следующие данные в произвольном порядке, разделенные пробелом:
Фамилия Имя Отчество датарождения номертелефона пол

Форматы данных:
фамилия, имя, отчество - строки
датарождения - строка формата dd.mm.yyyy
номертелефона - целое беззнаковое число без форматирования
пол - символ латиницей f или m.'''
from check_data import *

flag = True
while flag:
    try:
        #person_data = input('введите через пробел следующие данные о себе: Фамилия Имя Отчество датарождения номертелефона пол и нажмите Enter: ')
        person_data = "Иванов Иван Иванович 89131840501 23.01.2016 f"
        if person_data == "":
            raise Exception("вы не ввели данные!!! Попробуйте снова!!!")
        person_data_list = person_data.split()
        print(person_data_list)
        
        if len(person_data_list)>6:
            raise Exception("вы ввели данных больше, чем требуется: проверьте и введите заново: ")
        elif len(person_data_list)<6:
            raise Exception("вы ввели данных меньше, чем требуется: проверьте и введите заново: ")
        elif check_date_of_birth(person_data_list)[1] == False:
            raise Exception(check_date_of_birth(person_data_list)[0])
        elif check_gender(person_data_list)[1] == False:
            raise Exception(check_gender(person_data_list)[0])
        elif check_patronymic(person_data_list)[1] == False:
            raise Exception(check_patronymic(person_data_list)[0])
        elif check_phone_number(person_data_list)[1] == False:
            raise Exception(check_phone_number(person_data_list)[0])
        elif check_surname(person_data_list)[1] == False:
            raise Exception(check_surname(person_data_list)[0])
        
        else: 
            print("Вы ввели корректные данные, спасибо!!!")
            flag = False
        
        
    except Exception as e:
        print(e)

name_person = check_name(person_data_list.copy(), check_phone_number(person_data_list),check_date_of_birth(person_data_list), \
                 check_gender(person_data_list), check_surname(person_data_list), check_patronymic(person_data_list))  

'''
print(check_phone_number(person_data_list))
print(check_date_of_birth(person_data_list))
print(check_gender(person_data_list))
print(check_surname(person_data_list))
print(check_patronymic(person_data_list))

'''



