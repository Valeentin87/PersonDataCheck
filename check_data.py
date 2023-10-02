def check_phone_number(data_person):
    for data in data_person:
        if data.isdigit():
            return data, True
    return "номер телефона во введенных данных отсутствует", False

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

