
from tkinter import *
from tkinter import messagebox


def MenuCreate(menu_task:list,tearoff,font):
    new_menu = Menu(tearoff=tearoff,font=font)
    for item in menu_task:
        if(item[0]=='separator'):
            new_menu.add_separator()
        elif(item[0]=='sub'):
            new_menu.add_cascade(label=item[1], menu=MenuCreate(item[2],tearoff=item[3],font=item[4]))
        elif(item[0]==''):
            new_menu.add_cascade(label=item[1], command=item[2])
    return new_menu



def file_click():
    messagebox.showinfo("GUI Python", "Нажата опция File")


def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")


def view_click():
    messagebox.showinfo("GUI Python", "Нажата опция View")




root = Tk()
root.title("GUI на Python")
root.geometry("300x250+560+250")

# добавление меню к окну
root.config(menu=MenuCreate([
    ['','new',file_click],
    ['sub','sub',
    [
    ['separator'],
    ['','edit',edit_click],
    ['separator'],
    ['','edit',edit_click],
    ['separator']
    ],0,("Verdana", 15, "bold")],
    ['','edit',edit_click]
    
],0,("Verdana", 13, "bold"))
)

# отображение окна, запуск цикла обработки событий
root.mainloop()


