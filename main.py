import logging
import os

def decorate_foo(people):
    def decorate_around_people():
        logging.basicConfig(filename='Simplelog.log', filemode='w', level=logging.INFO,
                            format='%(asctime)s - %(funcName)s - %(message)s')
        logging.info(f'Функция стартовала ')
        print(people(user_input))
        result = people(user_input)
        logging.basicConfig(filename='Simplelog.log',filemode='w', level=logging.INFO,
                            format='%(asctime)s - %(message)s')
        logging.info(f'Функция завершила работу')
        path_of_log = os.path.abspath('Simplelog.log')
        logging.basicConfig(filename='Simplelog.log',filemode='w', level=logging.INFO,
                            format='%(asctime)s - %(message)s')
        logging.info(f'Путь к файлу {path_of_log}')
        logging.basicConfig(filename='Simplelog.log', filemode='w', level=logging.INFO,
                            format=f'%(asctime)s - %(message)s')
        logging.info(f'Функция вернула {result}')
    return decorate_around_people()


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': [ '2207 876234', '11-2' ],
    '2': [ '10006' ],
    '3': [ ]
}

user_input = input (str (
    'Введите одну из комманд: '
    '\np – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;'
    '\nl– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";'
    '\ns – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;'
    '\na – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,'
    ' имя владельца и номер полки, на котором он будет храниться.\n'))

@decorate_foo
def people(user_input):
    if user_input == 'p':
        user_input_people = input (str ('Введите номер документа: '))
        for n in documents:
            if n[ "number" ] == user_input_people:
                return (n[ 'name' ])
            else:
                print('Такого номера нет!')

def list():
    if user_input == 'l':
        for list_docs in documents:
            return (list_docs.values ())


def shelf():
    if user_input == 's':
        user_input_shelf = input (str ('Введите номер документа: '))
        for list_dir, list_docs in directories.items ():
            for list_docs_val in list_docs:
                if user_input_shelf == list_docs_val:
                    return (list_dir)
                else:
                    print('Такого документа нет')


def add():
    if user_input == 'a':
        user_input_number = input (str ('Введите номер документа: '))
        user_input_type = input (str ('Введите тип: '))
        user_input_name = input (str ('Введите имя владельца: '))
        user_input_directories = input (str ('Введите номер полки: '))
        documents.append ({'type': user_input_type, 'number': user_input_number, 'name': user_input_name})
        directories.update ({user_input_directories: [ user_input_number ]})
        return (directories)
        print('\n', documents)