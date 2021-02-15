from functions import *
from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title('Employee Evaluating system')
root.state('zoomed')
root.geometry('800x600')
root.iconbitmap("marios.ico")
bg = ImageTk.PhotoImage(Image.open('keo.jpg'))

first_window(root)

root.mainloop()