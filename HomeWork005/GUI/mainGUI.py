
from asyncio.windows_events import NULL
from operator import attrgetter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class FrameWithScrollBar(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg='yellow')
        self.frame = tk.Frame(self.canvas, bg='green')
        self.scrollbar = tk.Scrollbar(self, orient='vertical',
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self._frame_id = self.canvas.create_window(
                                 self.canvas.winfo_width(), 0,
                                 anchor='nw',
                                 window=self.frame)
        self.frame.bind('<Configure>', self.onFrameConfigure)
        self.canvas.bind('<Configure>', self.onCanvasConfigure)

    def onFrameConfigure(self, event):       
        self.canvas.configure(scrollregion=self.frame.bbox('all'))

    def onCanvasConfigure(self, event):
        width = event.width
        self.canvas.itemconfigure(self._frame_id, width=self.canvas.winfo_width())

class baseGUI():
    def MenuCreate(menu_task:list,tearoff,font):
        new_menu = Menu(tearoff=tearoff,font=font)
        for item in menu_task:
            if(item[0]=='separator'):
                new_menu.add_separator()
            elif(item[0]=='sub'):
                new_menu.add_cascade(label=item[1], menu=baseGUI.MenuCreate(item[2],tearoff=item[3],font=item[4]))
            elif(item[0]==''):
                new_menu.add_cascade(label=item[1], command=item[2])
        return new_menu
    
    def CreateElementTVShop(root,item):
        pass
        
        frameElement = Frame(root,borderwidth=1, relief="sunken")
        img = Image.open(item.manufacturer.filename)
        baseheight = 25
        hpercent = (baseheight/float(img.size[1]))
        wsize = int((float(img.size[0])*float(hpercent)))
        imgManufacturer = ImageTk.PhotoImage(img.resize((wsize,baseheight), Image.ANTIALIAS))  
        lbl_imageManufacturer = Label(frameElement, height=baseheight, image=imgManufacturer)
        lbl_imageManufacturer.image_ref = imgManufacturer
        lbl_imageManufacturer.pack(side=TOP,anchor=NE)

        frameTypeInfo = Frame(frameElement,borderwidth=1, relief="sunken")
        img = Image.open(item.type.base)
        basewidth = 250
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        imgType = ImageTk.PhotoImage(img.resize((basewidth,hsize), Image.ANTIALIAS))        
        lbl_imageType = Label(frameTypeInfo, width=250, image=imgType)
        lbl_imageType.image_ref = imgType
        lbl_imageType.pack(side=TOP)

        labelType = Label(frameTypeInfo,text=item.type.name, justify=LEFT)
        labelType.pack(side=TOP)
        frameTypeInfo.pack(side=LEFT)

        frameData = Frame(frameElement,borderwidth=1, relief="sunken")
        Label(frameData,text=f'Size: {item.type.size}', justify=LEFT).pack(side=TOP)
        Label(frameData,text=f'Resolution:{item.type.vertical} x {item.type.horizontal}', justify=LEFT).pack(side=TOP)
        Label(frameData,text=f'Price: {item.price}', justify=LEFT).pack(side=TOP)
        
        frameData.pack(side=LEFT)

        frameElement.obj = item

        return frameElement

class GUI_HW005_task01(baseGUI):
    root = 0
    current_punkt = 0
    def main_click():
        pass
        
        try:
            if(GUI_HW005_task01.root==0):
                pass
            else:
                GUI_HW005_task01.root.destroy()

        except Exception as ex:
            print("Общее исключение")
            print(ex)
        
        GUI_HW005_task01.root = Tk()
        GUI_HW005_task01.root.title("GUI на Python")
        GUI_HW005_task01.root.geometry("640x480+250+250")
        # добавление меню к окну
        GUI_HW005_task01.root.config(menu=baseGUI.MenuCreate([
        ['','Main',GUI_HW005_task01.main_click],
        
        ['sub','Exercises',
        [
        ['separator'],
        ['','Add TVShop',GUI_HW005_task01.addTVShop_click],
        ['separator'],
        ['','ShowList',GUI_HW005_task01.showList_click],
        ['','ShowTable',GUI_HW005_task01.showTable_click],
        ['separator'],
        ['','Sort by Price',GUI_HW005_task01.sortPrice_click],
        ['','Sort by Manufacturer and by Type',GUI_HW005_task01.sortManufacturerType_click]
        ],0,("Verdana", 10, "bold")]
        
        ,['','About',GUI_HW005_task01.about_click]
        ,['','Exit',exit]

        ],0,("Verdana", 13, "bold")))

      
        task = '''
\tРазработайте приложение Python с использованием Tkinter. для ввода данных об объекте класса Телевизор. Храните данные в бинарном файле с использованием модуля shelve.\n
\tДанные из таблицы выводите в метку Label с моноширинным шрифтом. Для добавления данных в таблицу используйте кнопку Button, команду меню.\n
\tКласс Телевизор с полями для хранения\n 
\t•	производителя и типа телевизора, это одно поле (используйте Combobox для выбора конкретного значения),\n 
\t•	диагональ экрана,\n 
\t•	разрешения по вертикали,\n 
\t•	разрешения по горизонтали,\n
\t•	наличие разъема CF\n
\t•	наличие разъема HDMI\n
\t•	наличие разъема USB\n 
\t•	цена.\n
\t Реализуйте обработки:\n
\t•	сортировка по убыванию цены\n
\t•	сортировка по производителю и типу\n
'''

        buttonFrame = Frame(GUI_HW005_task01.root)
        buttonFrame.pack(anchor=CENTER, fill=X, expand=False, side=BOTTOM)

      
        
        txtFrame = Frame(GUI_HW005_task01.root, borderwidth=1, relief="sunken")
        txtOutput = Text(txtFrame,  height = 17, width = 70, borderwidth=0)
        txtOutput.insert(INSERT, task)
        vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
        txtOutput['yscroll'] = vscroll.set

        vscroll.pack(side="right", fill="both")
        txtOutput.pack( fill="both", expand=True)

        txtFrame.pack( fill="both", expand=True)


        buttonCreate = Button(buttonFrame,text="Add", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
        buttonCreate.config(command=GUI_HW005_task01.addTVShop_click)
        buttonCreate.pack(side=LEFT,fill=X,expand=True)

        buttonShowListCollection = Button(buttonFrame,text="Show List", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
        buttonShowListCollection.config(command=GUI_HW005_task01.showList_click)
        buttonShowListCollection.pack(side=LEFT,fill=X,expand=True)

        buttonShowTableCollection = Button(buttonFrame,text="Show Table", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
        buttonShowTableCollection.config(command=GUI_HW005_task01.showTable_click)
        buttonShowTableCollection.pack(side=LEFT,fill=X,expand=True)

        buttonSortDescPrice = Button(buttonFrame,text="Sort Price", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
        buttonSortDescPrice.config(command=GUI_HW005_task01.sortPrice_click)
        buttonSortDescPrice.pack(side=LEFT,fill=X,expand=True)

        buttonSortManufacturerAndType = Button(buttonFrame,text="Sort Manufacturer", background="#555", foreground="#ccc", padx="15", pady="6", font="15")
        buttonSortManufacturerAndType.config(command=GUI_HW005_task01.sortManufacturerType_click)
        buttonSortManufacturerAndType.pack(side=LEFT,fill=X,expand=True)

        
        # отображение окна, запуск цикла обработки событий
        GUI_HW005_task01.root.mainloop()
        messagebox.showinfo("GUI Python", "Нажата опция Main")
        
    def addTVShop_click():
        pass
        messagebox.showinfo("GUI Python", "Нажата опция Add TVShop")

    def showList_click():
        pass
        GUI_HW005_task01.current_punkt=0
        try:
            if(GUI_HW005_task01.root==0):
                pass
            else:
                GUI_HW005_task01.root.destroy()

        except Exception as ex:
            print("Общее исключение")
            print(ex)
        
        GUI_HW005_task01.root = Tk()
        GUI_HW005_task01.root.title("GUI на Python")
        GUI_HW005_task01.root.geometry("640x480+250+250")
        # добавление меню к окну
        GUI_HW005_task01.root.config(menu=baseGUI.MenuCreate([
        ['','Main',GUI_HW005_task01.main_click],
        
        ['sub','Exercises',
        [
        ['separator'],
        ['','Add TVShop',GUI_HW005_task01.addTVShop_click],
        ['separator'],
        ['','ShowList',GUI_HW005_task01.showList_click],
        ['','ShowTable',GUI_HW005_task01.showTable_click],
        ['separator'],
        ['','Sort by Price',GUI_HW005_task01.sortPrice_click],
        ['','Sort by Manufacturer and by Type',GUI_HW005_task01.sortManufacturerType_click]
        ],0,("Verdana", 10, "bold")]
        
        ,['','About',GUI_HW005_task01.about_click]
        ,['','Exit',exit]

        ],0,("Verdana", 13, "bold")))

        listbox = Listbox(GUI_HW005_task01.root, font = ("Courier", 13, "bold"))
        listbox.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)
        
        def select(evt):
            event = evt.widget
            output = []
            selection = event.curselection()
            #.curselection() returns a list of the indexes selected
            #need to loop over the list of indexes with .get()
            for i in selection:
                o = listbox.get(i)
                item = GUI_HW005_task01.collection[i]
                output.append(item.type.name)
            messagebox.showinfo("Listbox Select", output)
        listbox.bind('<<ListboxSelect>>',select)
        
        # объект для организации прокрутки по вертикали
        scrollbarY = Scrollbar(listbox)
        scrollbarY.pack(side=RIGHT, fill=Y)

        # завершение настройки прокрутки по вертикали, передать объекту
        # прокрутки метод прокрутки по вертикали из listbox
        scrollbarY.config(command=listbox.yview)

        # связь листбокса и объекты прокрутки
        listbox.config(yscrollcommand=scrollbarY.set)

        # объект для организации прокрутки по вертикали
        scrollbarX = Scrollbar(listbox,orient=HORIZONTAL)
        scrollbarX.pack(side=BOTTOM, fill=X)

        # завершение настройки прокрутки по вертикали, передать объекту
        # прокрутки метод прокрутки по вертикали из listbox
        scrollbarX.config(command=listbox.xview)

        # связь листбокса и объекты прокрутки
        listbox.config(xscrollcommand=scrollbarX.set)

        for item in GUI_HW005_task01.collection:
            # добавляем в список начальные элементы
            listbox.insert(END,item)
        listbox.pack(side=TOP,fill='both',expand=True)
        messagebox.showinfo("GUI Python", "Нажата опция Show List")

    def showTable_click():
        pass
        GUI_HW005_task01.current_punkt=1
        try:
            if(GUI_HW005_task01.root==0):
                pass
            else:
                GUI_HW005_task01.root.destroy()

        except Exception as ex:
            print("Общее исключение")
            print(ex)
        
        GUI_HW005_task01.root = Tk()
        GUI_HW005_task01.root.title("GUI на Python")
        GUI_HW005_task01.root.geometry("640x480+250+250")
        # добавление меню к окну
        GUI_HW005_task01.root.config(menu=baseGUI.MenuCreate([
        ['','Main',GUI_HW005_task01.main_click],
        
        ['sub','Exercises',
        [
        ['separator'],
        ['','Add TVShop',GUI_HW005_task01.addTVShop_click],
        ['separator'],
        ['','ShowList',GUI_HW005_task01.showList_click],
        ['','ShowTable',GUI_HW005_task01.showTable_click],
        ['separator'],
        ['','Sort by Price',GUI_HW005_task01.sortPrice_click],
        ['','Sort by Manufacturer and by Type',GUI_HW005_task01.sortManufacturerType_click]
        ],0,("Verdana", 10, "bold")]
        
        ,['','About',GUI_HW005_task01.about_click]
        ,['','Exit',exit]

        ],0,("Verdana", 13, "bold")))

        # --- create canvas with scrollbar ---
        canvas = Canvas(GUI_HW005_task01.root)
        canvas.pack(side=LEFT,fill='both',expand=True)

        scrollbar = Scrollbar(GUI_HW005_task01.root, command=canvas.yview)
        scrollbar.pack(side=LEFT, fill='y')

        canvas.configure(yscrollcommand = scrollbar.set)

        def on_configure(event):
            # update scrollregion after starting 'mainloop'
            # when all widgets are in canvas
            canvas.configure(scrollregion=canvas.bbox('all'))

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.bind('<Configure>', on_configure)

        # --- put frame in canvas ---
        frame = Frame(canvas)
        canvas.create_window((0,0), window=frame, anchor='nw')

        def select(evt):
            event = evt.widget
            while not hasattr(event, 'obj'):
                event=event.master
            item = event.obj
            messagebox.showinfo("Listbox Select", item.type.name)

        cnt = len(GUI_HW005_task01.collection)
        columns = 2
        rows = round(cnt/columns)
        tmp_height = 0
        for r in range(0, rows):
            for c in range(0, columns):
                pos = r*columns+c
                if(cnt>pos):
                    element = baseGUI.CreateElementTVShop(frame, GUI_HW005_task01.collection[pos])
                    element.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)
                    element.bind_all('<Button>', select)
                    element.update_idletasks()
                    if(tmp_height==0):
                        tmp_height=element.winfo_height()
        
        frame.update_idletasks()
        GUI_HW005_task01.root.update_idletasks()
        GUI_HW005_task01.root.geometry("{}x{}".format(frame.winfo_width(), 2*tmp_height+30))

        messagebox.showinfo("GUI Python", "Нажата опция Show Table")

    def sortPrice_click():
        pass
        messagebox.showinfo("GUI Python", "Нажата опция Sort Price")
        GUI_HW005_task01.collection = sorted(GUI_HW005_task01.collection,key=attrgetter('price'),reverse=TRUE)
        if(GUI_HW005_task01.current_punkt==0):
            pass
            GUI_HW005_task01.showList_click()
        elif(GUI_HW005_task01.current_punkt==1):
            pass
            GUI_HW005_task01.showTable_click()

    def sortManufacturerType_click():
        pass
        messagebox.showinfo("GUI Python", "Нажата опция Sort Manufacturer and Type")
        GUI_HW005_task01.collection = sorted(GUI_HW005_task01.collection,key=attrgetter('manufacturer.name','type.name'))
        if(GUI_HW005_task01.current_punkt==0):
            pass
            GUI_HW005_task01.showList_click()
        elif(GUI_HW005_task01.current_punkt==1):
            pass
            GUI_HW005_task01.showTable_click()

    def about_click():
        pass
        try:
            if(GUI_HW005_task01.root==0):
                pass
            else:
                GUI_HW005_task01.root.destroy()

        except Exception as ex:
            print("Общее исключение")
            print(ex)
        
        GUI_HW005_task01.root = Tk()
        GUI_HW005_task01.root.title("GUI на Python")
        GUI_HW005_task01.root.geometry("640x480+250+250")
        # добавление меню к окну
        GUI_HW005_task01.root.config(menu=baseGUI.MenuCreate([
        ['','Main',GUI_HW005_task01.main_click],
        
        ['sub','Exercises',
        [
        ['separator'],
        ['','Add TVShop',GUI_HW005_task01.addTVShop_click],
        ['separator'],
        ['','ShowList',GUI_HW005_task01.showList_click],
        ['','ShowTable',GUI_HW005_task01.showTable_click],
        ['separator'],
        ['','Sort by Price',GUI_HW005_task01.sortPrice_click],
        ['','Sort by Manufacturer and by Type',GUI_HW005_task01.sortManufacturerType_click]
        ],0,("Verdana", 10, "bold")]
        
        ,['','About',GUI_HW005_task01.about_click]
        ,['','Exit',exit]

        ],0,("Verdana", 13, "bold")))

      
        task = '''
\tДомашняя работа по Python.\n
\n
\tВыполнил ст.гр. ВПУ-911\n
\tХижняк Павел\n 
\n
\tПреподователь\n 
\tЛычагин Владислав\n 
\n 
\n
\tДонецк - 2022 год\n
'''
   
        
        txtFrame = Frame(GUI_HW005_task01.root, borderwidth=1, relief="sunken")
        txtOutput = Text(txtFrame,  height = 17, width = 70, borderwidth=0)
        txtOutput.insert(INSERT, task)
        vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
        txtOutput['yscroll'] = vscroll.set

        vscroll.pack(side="right", fill="both")
        txtOutput.pack( fill="both", expand=True)

        txtFrame.pack( fill="both", expand=True)

        
        # отображение окна, запуск цикла обработки событий
        GUI_HW005_task01.root.mainloop()
        messagebox.showinfo("GUI Python", "Нажата опция About")
        
    def Show(list_items):
        GUI_HW005_task01.collection = list_items
        GUI_HW005_task01.main_click()
          

        

