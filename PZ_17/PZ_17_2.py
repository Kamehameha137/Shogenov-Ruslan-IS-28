from tkinter import *
from tkinter import ttk

root = Tk()   
root.title("PZ-17, Номер 2, Вариант 30")
root.geometry("300x100")  

def calculate():
     value = float(entry1.get())
     result = value / 100
     entry2.delete(0, END)
     entry2.insert(0, str(result)) 

label1 = ttk.Label(text="Сколько сантиметров:")
label2 = ttk.Label(text="Перевод в метры:")
label1.grid(row=1)
label2.grid(row=3)

entry1 = ttk.Entry()
entry1.grid(row=1, column=1)
entry2 = ttk.Entry()
entry2.grid(row=3, column=1)

buton1 = ttk.Button(text="Перевести", command=calculate)
buton1.grid(row=2)




    

root.mainloop()