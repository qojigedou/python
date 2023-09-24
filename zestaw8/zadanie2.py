import PyPDF2  # pip install PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import Text
from tkinter import Menu

okno = tk.Tk()
okno.title("My PDF text extractor")
okno.geometry("750x450")

# dodać widget Text i umieściś z jakimś marginesem
text = Text(okno, height = 500, width = 300, padx=15, pady=15)
text.pack()
def clear_text():
   text.delete(1.0, tk.END)

def open_pdf():
   file = filedialog.askopenfilename(title="Select a PDF", filetypes=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      pdf_file= PyPDF2.PdfReader(file)
      for i in range(len(pdf_file.pages)):
         page = pdf_file.pages[i]
         content=page.extract_text()
         text.insert(tk.END, content)

def quit_app():
   okno.destroy()

menu = Menu(okno)
okno.config(menu = menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label = "Open", command=open_pdf)
file_menu.add_command(label = "Clear", command=clear_text)
file_menu.add_command(label = "Quit", command=quit_app)

# utworzyć widget Menu i jego strukturę jak na rysunku
# Open powinno wołać open_pdf
# Clear powinno wołać clear_text
# Quit powinno wołać quit_app


okno.mainloop()