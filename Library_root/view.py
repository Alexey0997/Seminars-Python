# VIEW - модуль ввода-вывода данных, через который пользователь управляет программой
from controller import * 
# Вводим список классов, подлежащих программному учету. 

# СВЕДЕНИЯ ПО УЧЕТНЫМ ДАННЫМ, ИСПОЛЬЗУЕМЫМ В ФУНКЦИЯХ.
class_numbers = ['7А', '7Б', '8А', '8Б']
subject_list = ['математика', 'русский язык', 'литература']
mark_list = [1, 2, 3, 4, 5]

# ФУНКЦИЯ ЗАПРОСА НОМЕРА КЛАССА
# def input_class():
#     return input('С каким классом работаем? ').upper()

def input_class():
    print(f'\nВ программе ведется учет успеваемости учеников 7А, 7Б, 8А и 8Б классов.') 
    num = str(input('С каким классом работаем? ')).replace(' ', '').upper()
    valid = False
    for item in class_numbers:
        if num == item:
            valid = True
    if valid == True:
        return num
    else:    
        print(f'\nУчет ведется на 7А, 7Б, 8А и 8Б классы. Сведениями о {num} не располагаем.')
        input_class()




# ФУНКЦИЯ ВЫБОРА УЧЕБНОЙ ДИСЦИПЛИНЫ
# def input_subject():
#     return input('\n\tКакой предмет? ').lower()

def input_subject():
    sub = str(input('\nКакой предмет? ')).lower()
    valid = False
    for item in subject_list:
        if sub == item:
            valid = True
    if valid == True:
        return sub
    else:    
        print(f'\nУчет ведется по следующим дисциплинам:\n\
            \t- русский язык;\n\
            \t- литература;\n\
            \t- математика.\n"{sub.upper()}" не подлежит учету в данной программе.')
        input_subject()
    return

# ФУНКЦИЯ ФОРМИРОВАНИЯ СПИСКА УЧЕНИКОВ С ОЦЕНКАМИ ПО ПРЕДМЕТУ
def list_of_child(journal: dict): 
    for i, child in enumerate(journal, 1): 
        print(f'{i}. {child:20} {journal.get(child)}')
# Печатаем:   № п/п, ФИ ученика, оценки по предмету
   
# ФУНКЦИЯ ОПРОСА УЧЕНИКА
# def who_answer():
#     return input('\nКто будет отвечать? ')

def who_answer():
    print('\n\tДля выхода из программы введите "выход".\n\
        Для опроса ученика введите его фамилию и имя.')
    deсision = input('\tВведите нужные данные: ')
    return deсision

# ФУНКЦИЯ ВЫСТАВЛЕНИЯ ОЦЕНКИ
# def what_mark():
#     return input('Какая оценка за ответ? ')

def what_mark():
    mark = int(input('Поставьте оценку за ответ от 1 до 5 баллов: '))
    valid = False
    for i in mark_list:
        if i == mark:
            valid = True
    if valid == True:
        print(mark)
        return mark
    else:
        print('Такая оценка не предусмотрена методикой. Держите себя в руках:)')
        what_mark()
    return

