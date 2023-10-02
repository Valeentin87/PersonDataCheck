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
        person_data = input('введите через пробел следующие данные о себе: Фамилия Имя Отчество датарождения номертелефона пол и нажмите Enter: ')
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

print(check_phone_number(person_data_list))
    
