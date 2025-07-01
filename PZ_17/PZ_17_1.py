from tkinter import *
from tkinter import ttk

root = Tk()   
root.title("PZ-17, Вариант 30")
root.geometry("626x612")  
root["bg"] = "#ffadb2"

KeyArgs_grid_pos = {"sticky": "W", "padx": 8, "column": 0} 
KeyArgs_grid_font = {"font": ("Arial", 12), "background":root["bg"]}
KeyArgs_grid_entry = {"sticky":W, "padx":250}



label1 = ttk.Label(text="Регистрационная страница электронной библиотеки", font=("Arial", 12,"bold"), background=root["bg"])
label2 = ttk.Label(text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой", **KeyArgs_grid_font)

label1.grid(row=1, **KeyArgs_grid_pos, pady=6)
label2.grid(row=2, **KeyArgs_grid_pos, pady=12)



label3 = ttk.Label(text="Введите регистрационное имя:", **KeyArgs_grid_font)
label4 = ttk.Label(text="Введите пароль:", **KeyArgs_grid_font)
label5 = ttk.Label(text="Подтвердите пароль:", **KeyArgs_grid_font)
label3.grid(row=3, **KeyArgs_grid_pos,)
label4.grid(row=4, **KeyArgs_grid_pos)
label5.grid(row=5, **KeyArgs_grid_pos)

entry1 = ttk.Entry()
entry2 = ttk.Entry()
entry3 = ttk.Entry()
entry1.grid(row=4, **KeyArgs_grid_entry)
entry2.grid(row=3, **KeyArgs_grid_entry)
entry3.grid(row=5, **KeyArgs_grid_entry)



label6 = ttk.Label(text="Ваш возраст:", **KeyArgs_grid_font)
label6.grid(row=6, **KeyArgs_grid_pos, pady=12)

rad_butt1 = Radiobutton(text="До 20", background=root["bg"])
rad_butt2 = Radiobutton(text="20-30", background=root["bg"])
rad_butt3 = Radiobutton(text="30-50", background=root["bg"])
rad_butt4 = Radiobutton(text="старше 50", background=root["bg"])
rad_butt1.grid(row=6, sticky=W ,padx=120)
rad_butt2.grid(row=6, sticky=W ,padx=180)
rad_butt3.grid(row=6, sticky=W ,padx=240)
rad_butt4.grid(row=6, sticky=W ,padx=300)



label6 = ttk.Label(text="На каких языках читаете:", **KeyArgs_grid_font)
label6.grid(row=7, **KeyArgs_grid_pos)

che_butt6 = Checkbutton(text="русский", background=root["bg"])
che_butt7 = Checkbutton(text="английский", background=root["bg"])
che_butt8 = Checkbutton(text="французский", background=root["bg"])
che_butt9 = Checkbutton(text="немецкий", background=root["bg"])
che_butt6.grid(row=7, sticky=W, padx=200)
che_butt7.grid(row=7, sticky=W, padx=270)
che_butt8.grid(row=7, sticky=W, padx=370)
che_butt9.grid(row=7, sticky=W, padx=470)



label7 = ttk.Label(text="Какой формат данных является для вас болле предпочтительным:", **KeyArgs_grid_font)
label7.grid(row=8, **KeyArgs_grid_pos, pady=12)

combobox = ttk.Combobox(values=["HTML", "Plain text"], state="readonly")
combobox.grid(row=9, sticky=W, padx=10)



label8 = ttk.Label(text="Ваши любимые авторы:", **KeyArgs_grid_font)
label8.grid(row=10, **KeyArgs_grid_pos, pady=20)

text = Text(width=30, height=5)
text.grid(row=11, **KeyArgs_grid_pos)

btn1 = ttk.Button(text = "OK")
btn2 = ttk.Button(text = "Отменить")
btn1.grid(row=12, sticky=W, padx=40)
btn2.grid(row=12, sticky=W, padx=140)



label8 = ttk.Label(text="Проверка PHP Лабораторные по базам данных:", **KeyArgs_grid_font)
label8.grid(row=13, **KeyArgs_grid_pos, pady=20)

btn3 = ttk.Button(text = "Лабораторные по базам данных", width=100)
btn3.grid(row=14, sticky=W, padx=8)

root.mainloop()