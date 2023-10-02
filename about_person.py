''' Напишите приложение, которое будет запрашивать у пользователя следующие данные в произвольном порядке, разделенные пробелом:
Фамилия Имя Отчество датарождения номертелефона пол

Форматы данных:
фамилия, имя, отчество - строки
датарождения - строка формата dd.mm.yyyy
номертелефона - целое беззнаковое число без форматирования
пол - символ латиницей f или m.'''
flag = True
while flag:
    try:
        #person_data = input('введите через пробел следующие данные о себе: Фамилия Имя Отчество датарождения номертелефона пол и нажмите Enter: ')
        person_data = "Иванов Иван Иванович 89131840501 23.01.2014 f"
        if person_data == "":
            raise Exception("вы не ввели данные!!! Попробуйте снова!!!")
        person_data_list = person_data.split()
        print(person_data_list)
        
        if len(person_data_list)>6:
            raise Exception("вы ввели данных больше, чем требуется: проверьте и введите заново: ")
        elif len(person_data_list)<6:
            raise Exception("вы ввели данных меньше, чем требуется: проверьте и введите заново: ")
        
        else: 
            print("Вы ввели корректные данные, спасибо!!!")
            flag = False
        
        
    except Exception as e:
        print(e)

def check_phone_number(data_person):
    for data in data_person:
        if data.isdigit():
            return data, True
    return "номер телефона в введенных данных отсутствует", False

def check_date_of_birth(data_person):
    for data in data_person:
        if len(data) == 10 and data[2] == '.' and data[5] == '.':
            if 0<int(data[0:2])<=31:
                if 0<int(data[3:5])<=12:
                    if int(data[6:]):
                        return data, True
    return "дата рождения во введенных данных отсутствует или введена не корректно!!! " 

def check_gender(data_person):
    for data in data_person:
        if data in ['f', 'm']:
            return data, True
    return "во введенных данных отсутствуют данные о гендерной принадлежности, либо они введены не верно!!! "

def check_surname(data_person):
    for data in data_person:
        if data.isalpha() and (data[-2:] in ['ан', 'ын', 'ин', 'их', 'ов', 'ев', 'ой', 'ой', 'их', 'ых']):
            return data.capitalize(), True
    return "Фамилии во введенных данных не обнаружено!!! ", False

def check_patronymic(data_person):
    for data in data_person:
        if data.isalpha() and (data[-2:] in ['ич', 'на']):
            return data.capitalize(), True
    return "Отчества во введенных данных не обнаружено!!! ", False

set_data_person = set()



def check_name(list, *args):
    for n in args:
        if n[1] == True:
            list.remove(n[0])
    return list
   


print(check_phone_number(person_data_list))
print(check_date_of_birth(person_data_list))
print(check_gender(person_data_list))
print(check_surname(person_data_list))
print(check_patronymic(person_data_list))

print(check_name(person_data_list.copy(), check_phone_number(person_data_list),check_date_of_birth(person_data_list), \
                 check_gender(person_data_list), check_surname(person_data_list), check_patronymic(person_data_list)))
print(person_data_list)