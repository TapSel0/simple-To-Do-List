from tkinter import *


root = Tk()
root.title("ToDoList")  # название окна

todo_list = Listbox(root, height=10, width=30)  # колоночка для запланированных дел
in_progress_list = Listbox(root, height=10, width=30)  # колонка для дел в процессе
complete_list = Listbox(root, height=10, width=30)  # колонка для выполненных дел

todo_list.grid(row=0, column=0, padx=5, pady=5)  # размещение по сетке с добавлением отступов
in_progress_list.grid(row=0, column=1, padx=5, pady=5)
complete_list.grid(row=0, column=2, padx=5, pady=5)

label_add_task = Label(root, text="Add task: ")  # надпись
label_add_task.grid(row=1, column=0, pady=5)  # размещение надписи

entry_add = Entry(root, width=30)  # поле ввода дел
entry_add.grid(row=1, column=1, pady=5)

button_add = Button(root, text="Add", width=10)  # кнопка для добавления
button_add.grid(row=1, column=2, pady=5)

root.mainloop()  # отрисовка окна
