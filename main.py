from tkinter import *


# функция добавления задачи
def create_task(event):
    task = entry.get()  # получение значения из ввода
    if task:
        todo_list.insert(END, task)  # добавление задачи в конец списка (END)
        entry.delete(0, END)  # очистка поля ввода от 0 до конечного символа


# функция перемещения задачи из одного столбца в другой
def move_task(event, source_list, target_list):
    selected_task = source_list.curselection()  # номер выбранной задачи
    target_list.insert(END, source_list.get(selected_task))  # добавление выбранной задачи в след. лист
    source_list.delete(selected_task)  # удачление задачи из предыдущего листа


root = Tk()
root.title("ToDoList")  # название окна

# Создание списков задач
todo_list = Listbox(root, height=10, width=30)  # колоночка для запланированных дел
in_progress_list = Listbox(root, height=10, width=30)  # колонка для дел в процессе
done_list = Listbox(root, height=10, width=30)  # колонка для выполненных дел

# Расположение списков задач в окне
todo_list.grid(row=0, column=0, padx=5, pady=5)  # размещение по сетке с добавлением отступов
in_progress_list.grid(row=0, column=1, padx=5, pady=5)
done_list.grid(row=0, column=2, padx=5, pady=5)

# создание виджетов интерфейса
label_add_task = Label(root, text="Add task: ")  # надпись
label_add_task.grid(row=1, column=0, pady=5)  # размещение надписи

entry = Entry(root, width=30)  # поле ввода дел
entry.grid(row=1, column=1, pady=5)

button_add = Button(root, text="Add", width=10)  # кнопка для добавления
button_add.grid(row=1, column=2, pady=5)
button_add.bind("<Button-1>", create_task)  # забиндили функции на кнопку. Указываем её, как аргумент (то есть без скобок)

# бинды для перемещения задач из 1 и 2 списка в 2 и 3 соответственно
todo_list.bind("<Double-Button-1>", lambda a: move_task(a, todo_list, in_progress_list))
in_progress_list.bind("<Double-Button-1>", lambda a: move_task(a, in_progress_list, done_list))

root.mainloop()  # запуск главного цикла событий
