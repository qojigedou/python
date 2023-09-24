from tkinter import Label, StringVar, Button, PhotoImage, Entry, filedialog, Frame
import tkinter as tk 
from PIL import Image
import PIL.Image
# if not hasattr(PIL.Image, 'Resampling'):  # Pillow<9.0
#     PIL.Image.Resampling = PIL.Image

okno = tk.Tk()
okno.title("Image resizer")
# okno.geometry("750x450")
okno.resizable(False, False)
# tytuł, geometria, nieskalowalne

image_fp = None  
data_image = None
photo_image = None

def open_handler():
	global image_fp, data_image
	image_fp = filedialog.askopenfilename(initialdir=".", filetypes=(("Image resizer", "*.png"),))
	if image_fp:
		data_image = PhotoImage(file=image_fp)
		image_label.config(image=data_image)

def width_modified(event):
	global image_fp
	if image_fp:
		w = width_entry.get()
		if w != "" and w.isdigit():
			w = int(w)
			image = Image.open(image_fp)
			image_width = image.width
			image_height = image.height
			width_percentage = int((w*100)/image_width)
			height_set_to = int(image_height * (width_percentage/100))
			height_entry_str.set(str(height_set_to))

def height_modified(event):
	global image_fp
	if image_fp:
		h = height_entry.get()
		if h != "" and h.isdigit():
			h = int(h)
			image = Image.open(image_fp)
			image_width = image.width
			image_height = image.height
			height_percentage = int((h*100)/image_height)
			width_set_to = int(image_width * (height_percentage/100))
			width_entry_str.set(str(width_set_to))

def resize_handler():
	global image_fp, photo_image
	if image_fp:
		w = width_entry_str.get()
		h = height_entry_str.get()

		if w != "" and w.isdigit() and h != "" and h.isdigit():
			w = int(w)
			h = int(h)
			image = Image.open(image_fp)
			image.thumbnail((w,h), Image.LANCZOS)
			image.save('temp.png')
			photo_image = PhotoImage(file='temp.png')
			image_label.config(image=photo_image)

def save_handler():
	global image_fp, photo_image
	if image_fp:
		image_save_fp = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG files","*.png"),), defaultextension=".png")
		if image_save_fp:
			w = width_entry_str.get()
			h = height_entry_str.get()
			if w != "" and w.isdigit() and h != "" and h.isdigit():
				w = int(w)
				h = int(h)
				image = Image.open(image_fp)
				image.thumbnail((w,h), Image.Resampling.LANCZOS)
				image.save(image_save_fp.name)


controls_frame = Frame(okno)

open_bnt = Button(controls_frame, command=open_handler, text="Open")
open_bnt.pack(side="left", pady=2)

width_label = Label(controls_frame, text="Width")
width_label.pack(side="left", pady=2)

width_entry_str = StringVar()
width_entry = Entry(controls_frame, textvariable="width_entry_str")
width_entry.bind("<KeyRelease>", width_modified)
width_entry.pack(side="left", pady=2)

height_label = Label(controls_frame, text="Height")
height_label.pack(side="left", pady=2)
height_entry_str = StringVar()
height_entry = Entry(controls_frame, textvariable="height_entry_str")
height_entry.pack(side="left", pady=2)
height_entry.bind("<KeyRelease>", height_modified)

resize_btn = Button(controls_frame, command=resize_handler, text="Resize")
resize_btn.pack(side="left", pady=2)

save_btn = Button(controls_frame, command=save_handler, text="Save")
save_btn.pack(side="left", pady=2)

controls_frame.pack()

image_label = Label(okno)
image_label.config(image="")
image_label.pack(fill="both", side="bottom")

okno.mainloop()
