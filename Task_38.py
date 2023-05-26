import input

def select_action():
    file = input.get_value('адрес файла')
    actions = {'вывод': print_data, 'запись': add_data, 'поиск': search_data,
               'изменение': change_data, 'удаление': delete_data}

    while True:
        action = input.get_value("действие: 'вывод', 'запись', 'поиск', " \
                                 "'изменение', 'удаление' данных или " \
                                 "'выход' из программы")
        if action in actions:
            actions[action](file)
        elif action == 'выход':
            break
        else:
            print('Вы ввели не действие.')

def print_data(file):
    with open(file, encoding='utf-8') as file:
        for line in file:
            length = len(line)
            if length > 2:
                print(line, end='')

def add_data(file):
    data = list()
    contacts = int(input.get_value('количество контактов для записи'))
    for i in range(1, contacts + 1):
        data.append(input.get_value('имя, фамилию, номер телефона и место ' \
                                    f'проживания {i} контакта через ' \
                                    'запятую с пробелом'))

    with open(file, 'a', encoding='utf-8') as file:
        for i in data:
            file.write(f'{i}\n')
        
def search_data(file):
    characteristic = input.get_value('характеристику')

    with open(file, encoding='utf-8') as file:
        is_contact_found = False
        for line in file:
            if characteristic in line.split(', '):
                print(line, end='')
                is_contact_found = True

        if not is_contact_found:
            print('Отсутствует контакт с данной характеристикой.')
            
def change_data(file):
    data = list()
    characteristic = input.get_value('характеристику')
    new_contact = input.get_value('новые имя, фамилию, номер телефона и ' \
                                  'место проживания контакта через запятую ' \
                                  'с пробелом')

    with open(file, encoding='utf-8') as file_read:
        for line in file_read:
            if characteristic in line.split(', '):
                data.append(new_contact)
            else:
                data.append(line)
    
    with open(file, 'w', encoding='utf-8') as file_write:
        for i in data:
            file_write.write(f'{i}\n')
          
def delete_data(file):
    data = list()
    characteristic = input.get_value('характеристику')

    with open(file, encoding='utf-8') as file_read:
        for line in file_read:
            if characteristic not in line.split(', '):
                data.append(line)

    with open(file, 'w', encoding='utf-8') as file_write:
        for i in data:
            file_write.write(f'{i}\n')


select_action()