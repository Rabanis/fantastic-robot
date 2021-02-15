from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import datetime

def g(onoma):
    root = Tk()
    root.title('Employee Evaluating system')
    #root.state('zoomed')
    root.geometry('500x400')
    root.configure(background = "#333333")

    var = StringVar()
    var.set("Admin's options:")

    def open_admin():
        if var.get() == "Admin's options:":
            return
        evalW = Toplevel()    

        if var.get() == "Create user":
            evalW.geometry("950x450")
            evalW.iconbitmap("marios.ico")
            evalW.configure(background = "#333333")
            evalW.title("Create user")
            create_user(evalW)
        
        
        elif var.get() == "Insert new elements":
            evalW.title("Insert LMNt")
            evalW.geometry("500x600")
            evalW.iconbitmap("marios.ico")
            evalW.configure(background = "#333333")
            insert_elements(evalW)
            

    def create_user(evalW):  
        #functions for inserting to the db tables.
        def add_manager():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()

            #creating the new user.
            user_values = "('"+username_entry.get()+"', '"+password_entry.get()+"', '"+name_entry.get()+"', '"+surname_entry.get()+"', '"+str(datetime.datetime.now())+"', '"+email_entry.get()+"');"
            my_cursor.execute("INSERT INTO user VALUES " + user_values)
            my_db.rollback()          #ΕΙΝΑΙ ΕΤΣΙ ΓΙΑ ΔΟΚΙΜΑΣΤΙΚΟΥΣ ΛΟΓΟΥΣ, ΝΑ ΤΟ ΑΛΛΑΞΩ ΟΤΑΝ ΤΟ ΤΕΛΕΙΩΣΩ ΣΕ COMMIT. AKΥΡΟ, ΠΑΛΙ ΤΑ ΚΑΤΕΓΡΑΨΕ Η ΜΑΛΑΚΙΑ >:(.
            #creating the new manager.
            manager_values = "('"+username_entry.get()+"', '"+special2_entry.get()+"', '"+special1_entry.get()+"');"
            my_cursor.execute("INSERT INTO manager VALUES " + manager_values)
            my_db.rollback()          #ΕΙΝΑΙ ΕΤΣΙ ΓΙΑ ΔΟΚΙΜΑΣΤΙΚΟΥΣ ΛΟΓΟΥΣ, ΝΑ ΤΟ ΑΛΛΑΞΩ ΟΤΑΝ ΤΟ ΤΕΛΕΙΩΣΩ ΣΕ COMMIT.

            #clearing the entry fields.
            username_entry.delete(0, 1000)
            password_entry.delete(0, 1000)
            name_entry.delete(0, 1000)  
            surname_entry.delete(0, 1000)
            email_entry.delete(0, 1000)
            special1_entry.delete(0, 1000)
            special2_entry.delete(0, 1000)
            employee1_entry.delete(0, 1000)
            employee2_entry.delete(0, 1000)
            employee3_entry.delete(0, 1000)
            employee4_entry.delete(0, 1000)

            feedback = Label(user_frame, text = "Manager added successfuly.", font = (15))
            feedback.grid(row = 9, column = 0, columnspan = 2)
            my_cursor.close
            my_db.close
            return

        def add_employee():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()

            #creating the new user.
            user_values = "('"+username_entry.get()+"', '"+password_entry.get()+"', '"+name_entry.get()+"', '"+surname_entry.get()+"', '"+str(datetime.datetime.now())+"', '"+email_entry.get()+"');"
            my_cursor.execute("INSERT INTO user VALUES " + user_values)
            my_db.rollback()          #ΕΙΝΑΙ ΕΤΣΙ ΓΙΑ ΔΟΚΙΜΑΣΤΙΚΟΥΣ ΛΟΓΟΥΣ, ΝΑ ΤΟ ΑΛΛΑΞΩ ΟΤΑΝ ΤΟ ΤΕΛΕΙΩΣΩ ΣΕ COMMIT.
            #creating the new employee
            employee_values = "('"+username_entry.get()+"', '"+employee1_entry.get()+"', '"+employee2_entry.get()+"', '"+employee3_entry.get()+"', '"+employee4_entry.get()+"');"
            my_cursor.execute("INSERT INTO employee VALUES " + employee_values)
            my_db.rollback()          #ΕΙΝΑΙ ΕΤΣΙ ΓΙΑ ΔΟΚΙΜΑΣΤΙΚΟΥΣ ΛΟΓΟΥΣ, ΝΑ ΤΟ ΑΛΛΑΞΩ ΟΤΑΝ ΤΟ ΤΕΛΕΙΩΣΩ ΣΕ COMMIT.

            #clearing the entry fields.
            username_entry.delete(0, 1000)
            password_entry.delete(0, 1000)
            name_entry.delete(0, 1000)  
            surname_entry.delete(0, 1000)
            email_entry.delete(0, 1000)
            special1_entry.delete(0, 1000)
            special2_entry.delete(0, 1000)
            employee1_entry.delete(0, 1000)
            employee2_entry.delete(0, 1000)
            employee3_entry.delete(0, 1000)
            employee4_entry.delete(0, 1000)


            feedback = Label(user_frame, text = "Employee added successfuly.", font = (15))
            feedback.grid(row = 9, column = 0, columnspan = 2)
            my_cursor.close
            my_db.close
            return

        def add_evaluator():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()

            #creating the new user.
            user_values = "('"+username_entry.get()+"', '"+password_entry.get()+"', '"+name_entry.get()+"', '"+surname_entry.get()+"', '"+str(datetime.datetime.now())+"', '"+email_entry.get()+"');"
            my_cursor.execute("INSERT INTO user VALUES " + user_values)
            my_db.rollback()          #ΕΙΝΑΙ ΕΤΣΙ ΓΙΑ ΔΟΚΙΜΑΣΤΙΚΟΥΣ ΛΟΓΟΥΣ, ΝΑ ΤΟ ΑΛΛΑΞΩ ΟΤΑΝ ΤΟ ΤΕΛΕΙΩΣΩ ΣΕ COMMIT.
            #creating the new evaluator.
            evaluator_values = "('"+username_entry.get()+"', '"+special2_entry.get()+"', '"+special1_entry.get()+"');"
            my_cursor.execute("INSERT INTO evaluator VALUES " + evaluator_values)
            my_db.rollback()          #ΕΙΝΑΙ ΕΤΣΙ ΓΙΑ ΔΟΚΙΜΑΣΤΙΚΟΥΣ ΛΟΓΟΥΣ, ΝΑ ΤΟ ΑΛΛΑΞΩ ΟΤΑΝ ΤΟ ΤΕΛΕΙΩΣΩ ΣΕ COMMIT.

            #clearing the entry fields.
            username_entry.delete(0, 1000)
            password_entry.delete(0, 1000)
            name_entry.delete(0, 1000)  
            surname_entry.delete(0, 1000)
            email_entry.delete(0, 1000)
            special1_entry.delete(0, 1000)
            special2_entry.delete(0, 1000)
            employee1_entry.delete(0, 1000)
            employee2_entry.delete(0, 1000)
            employee3_entry.delete(0, 1000)
            employee4_entry.delete(0, 1000)


            feedback = Label(user_frame, text = "Evaluator added successfuly.", font = (15))
            feedback.grid(row = 9, column = 0, columnspan = 2)  
            my_cursor.close
            my_db.close
            return

        #creating objects    
        user_frame = LabelFrame(evalW, text = "Add a new User!", padx = 3, pady = 3, bg = "orange")
        special_frame = LabelFrame(evalW, text = "Special fields", padx = 3, pady = 3, bg = "orange")
        employee_frame = LabelFrame(evalW, text = "Employee's special fields", padx = 3, pady = 3, bg = "orange")
        lbl_user1 = Label(user_frame, text = "New user's username:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_user2 = Label(user_frame, text = "New user's password:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_user3 = Label(user_frame, text = "New user's name:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_user4 = Label(user_frame, text = "New user's surname:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_user6 = Label(user_frame, text = "New user's email:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_special1 = Label(special_frame, text = "New user's firm (9 chars):", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_special2 = Label(special_frame, text = "Years of experience:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_employee1 = Label(employee_frame, text = "Employee's Bio:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_employee2 = Label(employee_frame, text = "Sistatikes:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_employee3 = Label(employee_frame, text = "Certificates:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_employee4 = Label(employee_frame, text = "Awards:", font = ("calibry",13), bg = "#76470C", fg = "snow")

        username_entry = Entry(user_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        password_entry = Entry(user_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        name_entry = Entry(user_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        surname_entry = Entry(user_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        email_entry = Entry(user_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        special1_entry = Entry(special_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        special2_entry = Entry(special_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        employee1_entry = Entry(employee_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        employee2_entry = Entry(employee_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        employee3_entry = Entry(employee_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")
        employee4_entry = Entry(employee_frame, borderwidth = 5, width = 40, bg = "#DDDDDD")

            #placing objects
        user_frame.grid(row = 0, column = 0, rowspan = 2, padx = 5, pady = 5)
        special_frame.grid(row = 1, column = 1, padx = 5, pady = 5)
        employee_frame.grid(row = 0, column = 1, padx = 5, pady = 5)
        lbl_user1.grid(row = 0, column = 0, padx = 5, pady = 7)
        lbl_user2.grid(row = 1, column = 0, padx = 5, pady = 7)
        lbl_user3.grid(row = 2, column = 0, padx = 5, pady = 7)
        lbl_user4.grid(row = 3, column = 0, padx = 5, pady = 7)
        lbl_user6.grid(row = 5, column = 0, padx = 5, pady = 7)
        lbl_special1.grid(row = 0, column = 0, padx = 5, pady = 7)
        lbl_special2.grid(row = 1, column = 0, padx = 5, pady = 7)
        lbl_employee1.grid(row = 0, column = 0, padx = 5, pady = 7)
        lbl_employee2.grid(row = 1, column = 0, padx = 5, pady = 7)
        lbl_employee3.grid(row = 2, column = 0, padx = 5, pady = 7)
        lbl_employee4.grid(row = 3, column = 0, padx = 5, pady = 7)

        username_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
        password_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
        name_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
        surname_entry.grid(row = 3, column = 1, padx = 5, pady = 5)
        email_entry.grid(row = 5, column = 1, padx = 5, pady = 5)
        special1_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
        special2_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
        employee1_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
        employee2_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
        employee3_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
        employee4_entry.grid(row = 3, column = 1, padx = 5, pady = 5)

            #creating buttons for each type of user:
        b_manager = Button(user_frame, command = add_manager)
        b_manager.configure(text = "Add new manager ", font = ("calibry",20), bg = "#888888")
        b_employee = Button(user_frame, command =add_employee)
        b_employee.configure(text = "Add new employee", font = ("calibry",20), bg = "#888888")
        b_evaluator = Button(user_frame, command = add_evaluator)
        b_evaluator.configure(text = "Add new evaluator ", font = ("calibry",20), bg = "#888888")

        #placing buttons.
        b_manager.grid(row = 6, column = 0, columnspan = 2, pady = 7, padx = 5)
        b_employee.grid(row = 7, column = 0, columnspan = 2, pady = 7, padx = 5)
        b_evaluator.grid(row = 8, column = 0, columnspan = 2, pady = 7, padx = 5)

    def insert_elements(evalW):
        #defining insertion functions.
        def insert_company():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()

            company_values1 = "('"+company_entry1.get()+"', '"+company_entry2.get()+"', '"+company_entry3.get()+"', '"+company_entry4.get()+"', "
            company_values2 = "'"+company_entry5.get()+"', '"+company_entry6.get()+"', '"+company_entry7.get()+"', '"+company_entry8.get()+"');"
            my_cursor.execute("INSERT INTO company VALUES " + company_values1 + company_values2)

            company_entry1.delete(0, 1000)
            company_entry2.delete(0, 1000)
            company_entry3.delete(0, 1000)
            company_entry4.delete(0, 1000)
            company_entry5.delete(0, 1000)
            company_entry6.delete(0, 1000)
            company_entry7.delete(0, 1000)
            company_entry8.delete(0, 1000)

            lbl = Label(frame_company, text = "New company has been inserted!", font = ("calibry", 15))
            lbl.grid(row = 9, column = 0, columnspan = 2)
            my_cursor.close
            my_db.close

            return

        def insert_antik():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')
            my_cursor = my_db.cursor()

            antik_values = "('"+antik_entry1.get()+"', '"+antik_entry2.get()+"', '"+antik_entry3.get()+"');"
            my_cursor.execute("INSERT INTO antikeim VALUES " + antik_values)

            antik_entry1.delete(0, 1000)
            antik_entry2.delete(0, 1000)
            antik_entry3.delete(0, 1000)

            lbl = Label(frame_antikeim, text = "New antikeim has been inserted!", font = ("calibry", 15))
            lbl.grid(row = 4, column = 0, columnspan = 2)
            my_cursor.close
            my_db.close
            return
        
        #creating objects.
        frame_company = LabelFrame(evalW, text = "New company's info",  padx = 3, pady = 3, bg = "orange")
        frame_antikeim = LabelFrame(evalW, text = "New antikeim info", padx = 3, pady = 5, bg = "orange")
        lbl_antik1 = Label(frame_antikeim, text = "antikeim's title:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_antik2 = Label(frame_antikeim, text = "antikeim's descr:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_antik3 = Label(frame_antikeim, text = "antikeim's origin:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company1 = Label(frame_company, text = "Company's afm:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company2 = Label(frame_company, text = "Company's DOY:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company3 = Label(frame_company, text = "Company's name:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company4 = Label(frame_company, text = "Company's phone:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company5 = Label(frame_company, text = "Company's street:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company6 = Label(frame_company, text = "Company's num:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company7 = Label(frame_company, text = "Company's city:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        lbl_company8 = Label(frame_company, text = "Company's country:", font = ("calibry",13), bg = "#76470C", fg = "snow")
        antik_entry1 = Entry(frame_antikeim, borderwidth = 5, width = 40, bg = "#DDDDDD")
        antik_entry2 = Entry(frame_antikeim, borderwidth = 5, width = 40, bg = "#DDDDDD")
        antik_entry3 = Entry(frame_antikeim, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry1 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry2 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry3 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry4 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry5 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry6 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry7 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")
        company_entry8 = Entry(frame_company, borderwidth = 5, width = 40, bg = "#DDDDDD")

        #placing objects.
        frame_company.grid(row = 0, column = 0, rowspan = 2, padx = 5, pady = 5)
        frame_antikeim.grid(row = 2, column = 0, padx = 5, pady = 5)
        lbl_antik1.grid(row = 0, column = 0, padx = 5, pady = 5)
        lbl_antik2.grid(row = 1, column = 0, padx = 5, pady = 5)
        lbl_antik3.grid(row = 2, column = 0, padx = 5, pady = 5)
        lbl_company1.grid(row = 0, column = 0)
        lbl_company2.grid(row = 1, column = 0)
        lbl_company3.grid(row = 2, column = 0)
        lbl_company4.grid(row = 3, column = 0)
        lbl_company5.grid(row = 4, column = 0)
        lbl_company6.grid(row = 5, column = 0)
        lbl_company7.grid(row = 6, column = 0)
        lbl_company8.grid(row = 7, column = 0, padx = 5)
        antik_entry1.grid(row = 0, column = 1)
        antik_entry2.grid(row = 1, column = 1)
        antik_entry3.grid(row = 2, column = 1)
        company_entry1.grid(row = 0, column = 1, pady = 2)
        company_entry2.grid(row = 1, column = 1, pady = 2)
        company_entry3.grid(row = 2, column = 1, pady = 2)
        company_entry4.grid(row = 3, column = 1, pady = 2)
        company_entry5.grid(row = 4, column = 1, pady = 2)
        company_entry6.grid(row = 5, column = 1, pady = 2)
        company_entry7.grid(row = 6, column = 1, pady = 2)
        company_entry8.grid(row = 7, column = 1, pady = 2)

        #creating buttons for insertion.
        companyButton = Button(frame_company, text = "Insert", command = insert_company)
        companyButton.configure(font = ("calibry", 15), bg = "#888888", width = 15)
        antikButton = Button(frame_antikeim, text = "Insert", command = insert_antik)
        antikButton.configure(font = ("calibry", 15), bg = "#888888", width = 15)

        companyButton.grid(row = 8, column = 0, columnspan = 2, pady = 10)
        antikButton.grid(row = 3, column = 0, columnspan = 2, pady = 10)
        return



    admin_menu = OptionMenu(root, var, "Create user", "Insert new elements")
    admin_menu.configure(background = "light blue", activebackground="cyan", font = ("calibry", 15))
    admin_menu.grid(row = 0, column = 0, padx = 170, pady = 20)

    my_btn = Button(root, text = "Click here once you choose.", font = ("calibry", 12), padx = 10, command = open_admin)
    my_btn.grid(row = 2, column = 0, padx = 20, pady = 50)

    root.mainloop()



#───────────────────────────────
#──────────▄▄▄▄▄▄▄▄▄▄▄──────────
#─────▄▄▀▀▀▀──────────▀▀▄▄──────
#───▄▀───────────────────▀▀▄────
#──█────────────────────────█───
#─█─────────────────────▄▀▀▀▀▀█▄
#█▀────────────────────█────▄███
#█─────────────────────█────▀███
#█─────▄▀▀██▀▄─────────█───────█
#█────█──████─█─────────▀▄▄▄▄▄█─
#█────█──▀██▀─█───────────────█─
#█────█───────█──────────────▄▀─
#█────▀▄─────▄▀──▄▄▄▄▄▄▄▄▄───█──
#█──────▀▀▀▀▀────█─█─█─█─█──▄▀──
#─█──────────────▀▄█▄█▄█▀──▄▀───
#──█──────────────────────▄▀────
#───▀▀▀▄──────────▄▄▄▄▄▄▀▀──────
#────▄▀─────────▀▀──▄▀──────────
#──▄▀───────────────█───────────
#─▄▀────────────────█──▄▀▀▀█▀▀▄─
#─█────█──█▀▀▀▄─────█▀▀────█──█─
#▄█────▀▀▀────█─────█────▀▀───█─
#█▀▄──────────█─────█▄────────█─
#█──▀▀▀▀▀█▄▄▄▄▀─────▀█▀▀▀▄▄▄▄▀──
#█───────────────────▀▄─────────
