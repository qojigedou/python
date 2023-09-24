import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar

okno = tk.Tk()
okno.title("PDF Reader")
okno.resizable(False, False)

string_var = tk.StringVar(okno, name="daytime")

def update_date_time():
	dzien = datetime.today().strftime('%W')
	miesiac = datetime.today().strftime('%B')
	rok = datetime.today().strftime('%Y')
	czas = datetime.today().strftime('%X')
	nazwa_dnia = datetime.today().strftime('%A')
	
	dt = "\n" + dzien + " " + miesiac + " " + rok + "\n" + nazwa_dnia + " " + czas + "\n"
	string_var.set(dt)
	
	date_time.after(1000, update_date_time)

date_time = Label(okno, bg = 'black', textvariable="daytime", fg="white", font=('Ariel', 45))
date_time.pack(anchor="center")

current_time = datetime.now()
day = current_time.strftime('%d')
month = current_time.strftime('%m')
year = current_time.strftime('%y')

cal = Calendar(okno, selectmode = "day",year = int(year), month = int(month), day = int(day))

update_date_time()
cal.pack(pady = 20)
okno.mainloop()