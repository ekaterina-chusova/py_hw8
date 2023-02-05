import model

def input_class():
    return input('\nС каким классом работаем? ').upper()

def input_subject():
    return input('\nВыберите предмет? Введите первые несколько букв. ').lower()

def who_answer():
    return input('\nКто будет отвечать? ')

def what_mark():
    return input('\nНа какую оценку ответил? ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def no_class():
    print('Такого класса нет в журнале. Введите название класса еще раз.\nИспользуйте русскую раскладку клавиатуры.')

def change_subject(sub: str):
    print('\nОткрыт предмет: ' + sub)

def no_subject():
    print('Такого предмета нет в журнале. Попробуйте еще раз.')

def no_mark():
    print('В журнале пятибальная шкала оценок.\nВведите цифру от 1 до 5.')
