from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

def o(onoma):
    root = Tk()
    root.title('Employee')
    #root.state('zoomed')
    root.geometry('500x400')
    root.configure(background = "#333333")

    var = StringVar()
    var.set("Employee's options:")

    def open():
        if var.get() == "Employee's options:":
            return
        evalW = Toplevel()
        evalW.configure(background = "#333333")

        if var.get() == "My profile":
            evalW.title("My Profile")
            evalW.geometry("600x600")
            create_profile(evalW, onoma)

        elif var.get() == "Request evaluation":
            evalW.title("Evaluation Request")
            evalW.geometry("800x800")
            create_request_evaluation_window(evalW, onoma)
            
        elif var.get() == "Show my requests":
            evalW.title("My requests")
            evalW.geometry("500x400")
            show_requests(evalW, onoma)
        
        #elif var.get() == "Cancel a request":
        #    #evalW = Toplevel()
        #    evalW.title("Available jobs")
        #    evalW.geometry("700x700")

    def create_profile(evalW, onoma):
        my_db = mysql.connector.connect(host = 'localhost', 
        user = "root", 
        password = '11111111', 
        database = 'evaluating')
        my_cursor = my_db.cursor()
        
        def confirm_password():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()
            
            my_cursor.execute("UPDATE user SET password = '"+edit_pass_entry.get()+"' WHERE username like '"+onoma+"'")

            edit_pass_entry.delete(0, 100)
            lbl = Label(frame_user, text = "changes saved.", font = ("calibry",13), bg = "#76470C", fg = "snow")
            lbl.grid(row = 6, column = 1, padx = 3, pady = 3)

            my_cursor.close
            my_db.close
            return

        my_cursor.execute("SELECT * FROM user WHERE username like '" + onoma +"'")
        my_result = my_cursor.fetchall()
        
        #creating objects
        frame_user = LabelFrame(evalW, text = "My profile", font = ("times new roman", 10), padx = 3, pady = 3, bg = "orange")
        lbl_username = Label(frame_user, text = "USERNAME: "+my_result[0][0], font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_password = Label(frame_user, text = "PASSWORD: "+my_result[0][1], font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_name = Label(frame_user, text = "NAME: "+my_result[0][2], font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_surname = Label(frame_user, text = "SURNAME: "+my_result[0][3], font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_reg_date = Label(frame_user, text = "REGISTRATION DATE:\n"+str(my_result[0][4]), font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_email = Label(frame_user, text = "E-MAIL: "+my_result[0][5], font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_edit_pass = Label(frame_user, text = "Edit your password:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        edit_pass_entry = Entry(frame_user, borderwidth = 5, width = 40, bg = "#DDDDDD")

        #placing objects
        frame_user.grid(row = 0, column = 0, padx = 5, pady = 5)
        lbl_username.grid(row = 1, column = 0, padx = 3, pady = 3)
        lbl_password.grid(row = 2, column = 0, padx = 3, pady = 3)
        lbl_name.grid(row = 3, column = 0, padx = 3, pady = 3)
        lbl_surname.grid(row = 4, column = 0, padx = 3, pady = 3)
        lbl_reg_date.grid(row = 5, column = 0, padx = 3, pady = 3)
        lbl_email.grid(row = 6, column = 0, padx = 3, pady = 3)
        lbl_edit_pass.grid(row = 3, column = 1, padx = 3, pady = 3)
        edit_pass_entry.grid(row = 4, column = 1, padx = 3, pady = 3)

        confirmB = Button(frame_user, command = confirm_password)
        confirmB.configure(text = "confirm changes ", font = ("calibry",10), bg = "#888888")
        confirmB.grid(row = 5, column = 1, padx = 3, pady = 3)

        my_cursor.close
        my_db.close
        return

    def create_request_evaluation_window(evalW, onoma):
        my_db = mysql.connector.connect(host = 'localhost', 
        user = "root", 
        password = '11111111', 
        database = 'evaluating')
        my_cursor = my_db.cursor()

        var = StringVar()
        dict = {}
        t = 0

        def request(job_id):
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()

            my_cursor.execute("INSERT INTO requestsevaluation VALUES ('"+onoma+"', '"+str(job_id)+"');")

            lbl = Label(my_frame, text = "Successful request.", font = ("calibri", 15))
            lbl.grid(row = 5, column = 1)

            my_cursor.close
            my_db.close
            return  

        #creating objects
        my_frame = LabelFrame(evalW, text = "", padx = 3, pady = 3, bg = "orange")



        #creating the radio buttons with options based on the job list.
        my_cursor.execute("SELECT id, position, evaluator FROM job")
        my_result = my_cursor.fetchall()
        for i in my_result:
            t += 1
            dict[t-1] = Radiobutton(my_frame, text = i[1], variable = var, value = t)
            dict[t-1].grid(row = t-1, column = 0, padx = 5, pady=2)
        
        #button for commitment.
        my_Button = Button(my_frame, command = lambda: request(var.get()))
        my_Button.configure(text = "Press once decided which job", font = ("calibry", 15))

        #placing objects
        my_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
        my_Button.grid(row = 2, column = 1, padx = 10, pady = 5)

        my_cursor.close
        my_db.close
        return

    def show_requests(evalW, onoma):
        my_db = mysql.connector.connect(host = 'localhost', 
        user = "root", 
        password = '11111111', 
        database = 'evaluating')
        my_cursor = my_db.cursor()

        def delete(id):
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()

            my_cursor.execute("DELETE FROM requestsevaluation WHERE job_id = '"+str(id)+"';")

            my_cursor.close
            my_db.close
            return

        #creating objects
        frame_request = LabelFrame(evalW, text = "my requests", font = ("times new roman", 10), padx = 3, pady = 3, bg = "orange")
        
        #placing objects
        frame_request.grid(row = 0, column = 0, padx = 5, pady = 5)

        
        #getting the list of the requests.
        my_cursor.execute("SELECT id, position FROM job INNER JOIN requestsevaluation WHERE requestsevaluation.job_id = job.id AND requestsevaluation.empl_usrname like '"+onoma+"' GROUP BY job.id;")
        my_result = my_cursor.fetchall()

        
        dict = {}
        butt_dict = {}
        t = 0
        var = IntVar()
        print(my_result)
        for i in my_result:
            dict[t] = Label(frame_request, text = "Job id is "+ str(i[0]) + " and position is: "+ i[1], font = ("calibry",13), bg = "#76470C", fg = "snow")
            dict[t].grid(row = t, column = 0, padx = 5, pady = 5)
            butt_dict[t] = Radiobutton(frame_request, text = "Delete request #"+str(i[0]),  variable = var, value = i[0])
            butt_dict[t].grid(row = t, column = 1, pady = 5)
            t += 1

        button = Button(frame_request, text = "Delete", font = ("calibry", 10), command = lambda: delete(var.get()))
        button.grid(row = t, column = 1)


        my_cursor.close
        my_db.close
        return

    employee_menu = OptionMenu(root, var, "My profile", "Request evaluation", "Show my requests")
    employee_menu.configure(background = "orange", activebackground="yellow")
    employee_menu.place(x = 55, y = 100)

    my_btn1 = Button(root, text = "Go.", font = ("calibry", 12), padx = 10, command = open)
    my_btn1.place(x = 230, y = 100)





    root.mainloop()


#░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░░░░░░░░░░
#░░░░░░░░░▄▄█████████████▄░░░░░░░░░░░░░░░
#░░░░░░░▄██████████████████░░░░░░░░░░░░░░
#░░░░░▄██████████████▀▀▀░▀██░░░░░░░░░░░░░
#░░░░▄██████▀▀▀▀▀▀░░░░░░░░▀██░░░░░░░░░░░░
#░░░░████████░░░░░░░░░░░░░░▀█░░░░░░░░░░░░
#░░░░████████░░░░░░░░░░░░░░▄█▄░░░░░░░░░░░
#░░░░████████░░░░░░░░░░▄░░███▀░░░░░░░░░░░
#░░░░░██████░░░░░█▀███▀▀░░░░░░░░░░░░░░░░░
#░░░░░███████░░░░░▀▀▀░░░░░░░░░░░░░░░░░░░░
#░░░░░▀█░░▀██░░░░░░░░░░▄░░░░▀░░░░░░░░░░░░
#░░░░░░▀▄░░▄▀░░░░░░░░░░░▄████▀░░░░░░░░░░░
#░░░░░░░░░░░░▄░░░░░░░░██▀█▄██░░░░░░░░░░░░
#░░░░░░░░░░░▀░░░░░░░░░░░▀▀▀▀▀░▀░░░░░░░░░░
#░░░░░░▄▄▄███░░░░░░░░░░░░░░░░░█▄░░░░░░░░░
#▄▄▄█████████▀░░░░░░░░▄▄░░░░▄▄█████▄▄▄░░░
#████████████░░░░░░░░░░██████████████████
#█████████████░░░▀░░░░░▄█████████████████
#██████████████░░░▄█▀▀█▀▀████████████████
