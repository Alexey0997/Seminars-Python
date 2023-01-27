# controller - это модуль сопряжения, обеспечивающий обмен данными между view & model

import view 
import model

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    student = ''
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit' or student == 'выход':
            break
        mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()
    