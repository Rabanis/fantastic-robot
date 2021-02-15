from tkinter import *
import tkinter
import mysql.connector

def a(onoma):
    root = Tk()
    root.state("zoomed")

    click = StringVar()
    click.set("epiloges")

    def choices():
        if click.get() == "change password":
            def ok_func():
                my_db = mysql.connector.connect(host = 'localhost', 
                user = "root", 
                password = '11111111', 
                database = 'evaluating')

                c = my_db.cursor()
                #c.execute(f"UPDATE user SET password = '{ch}' WHERE username = '{onoma}'")
                ch.destroy()
                ch_lbl.destroy()
                ok_butt.destroy()
                c.close()
                my_db.close()
            ch = Entry(root)
            ch_lbl = Label(root, text = "What's your new password?")
            ch_lbl.pack()
            ch.pack()
            ok_butt = Button(root, text = "OK", command = ok_func)
            ok_butt.pack()
        
    ntina = OptionMenu(root, click, "change password", "name", "surname", "reg_date", "email")
    ntina.pack()
    com_butt = Button(root, text = "commit", command = choices)
    com_butt.pack()

    root.mainloop()