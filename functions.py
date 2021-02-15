from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from functionsoffunctions import *
from employee_screen import *
from manager_page import *
from Evaluator_page import *
from admin_screen import *
b = ''
k = '#0d2950'
l = 'snow'

def first_window(master):
    global bg
    bg = ImageTk.PhotoImage(Image.open('keo.jpg'))
    my_l = Label(master, image = bg)
    my_l.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    frame = LabelFrame(master, text = 'Please connect to the system',font = ("Calibri", 30),bg = k, padx = 50, pady = 50, borderwidth = 5, fg = l)
    passwd_label = Label(frame, text = 'Please enter your Password: ', bg = k, fg = l)
    title_label = Label(master, text = 'Log in or Sign up: ', )
    usrn_label = Label(frame, text = 'Please enter your Username: ',fg = l, bg = k)
    usrname = Entry(frame, width = 40, bg = '#41e197')
    passwd = Entry(frame, bg = '#41e197',show = '*', width = 40)
    log_in = Button(frame, text = 'Log In:', bg = k, command = lambda: connect(usrname, passwd), fg = l)

    log_in.grid(row = 3, column = 0)
    frame.place(x = 150, y = 150)
    usrname.grid(row = 1, column = 1)
    usrn_label.grid(row = 1, column = 0)
    passwd.grid(row = 2, column = 1)
    passwd_label.grid(row = 2, column = 0)  
    

def connect(usrname, passwd):  

    my_db = mysql.connector.connect(host = 'localhost', 
    user = "root", 
    password = '11111111', 
    database = 'evaluating')

    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT username, password FROM user;")
    for i in my_cursor:
        if i[0]==usrname.get() and i[1]==passwd.get():
            if is_admin(i[0]) != None:
                g(i[0])
            if is_emoployee(i[0]) != None:
                o(i[0])
            if is_evaluator(i[0]) != None:
                a(i[0])
            if is_manager(i[0]) != None:
                p(i[0])
            
            my_db2 = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')

            c2 = my_db2.cursor()
            c2.execute(F"CREATE VIEW connected_user AS SELECT '{i[0]}' AS onoma")
            my_db2.commit()
            my_db2.close()
            c2.close()
            break
    my_cursor = my_db.cursor()
    my_cursor.close
    my_db.close






