import model
import view

def start():
    while True:
        class_path = view.input_class()
        resuil = model.control_class(class_path)
        if resuil > 0:
            model.set_class(class_path)
            break
        else:
            view.no_class()
    while True:       
        model.set_sublect(view.input_subject())
        res = model.open_file()
        if res != '0':
            view.change_subject(res)
            model.open_journal()
            break
        else:
            view.no_subject()
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit':
            break
        while True:
            mark = int(view.what_mark())
            res = model.control_mark(mark)
            if res != 0:
                model.students_mark(student, mark)
                break
            else:
                view.no_mark()
        # model.students_mark(student, mark)
    model.save_file() 