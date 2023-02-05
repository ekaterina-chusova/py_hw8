import os

journal = {}
subject = ''
path = ''

def set_class(class_path: str):
    global path
    path = 'Classes/' + class_path + '.txt'

def control_class(class_path: str):
    global path
    name = 'Classes'
    for filename in os.listdir(name):
        if class_path == filename.split('.')[0]:
            return 1
    return 0

def set_sublect(our_subject: str):
    global subject
    subject = our_subject

def open_file():
    global path
    global subject
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split('=')[0].startswith(subject):
            subject = sub.split('=')[0]
            # for study in sub.split(('='))[1].strip().split(', '):
            #     journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))
            return subject
    else:
        return '0'

def open_journal():
    global path
    global subject
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if subject == sub.split('=')[0]:
            for study in sub.split(('='))[1].strip().split(', '):
                journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))



def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split('=')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + '=' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))

def students_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks

def get_journal():
    return journal

def control_mark(mark: int):
    if mark > 0 and mark < 6:
        return 1
    else:
        return 0