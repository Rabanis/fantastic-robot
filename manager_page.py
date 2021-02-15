from tkinter import *
import mysql.connector
import tkinter

def p(onoma):
    root = Tk()
    def manager_first_page():

        clicked = StringVar()
        clicked.set("company's options")
        clicked2 = StringVar()
        clicked2.set('account options')

        def al_misthou():
            def p(epilogi):
                def b():
                    my_db2 = mysql.connector.connect(host = 'localhost', 
                    user = "root", 
                    password = '11111111', 
                    database = 'evaluating') 
                    c2 = my_db2.cursor()

                    c2.execute(f"UPDATE job SET salary = '{new_salary}' WHERE id = {epilogi}")
                    new_salary.destroy()
                    new_salary_lbl.destroy()
                    confirm_butt.destroy()
                    c2.close()
                    my_db2.close()


                new_salary_lbl = Label(root, text = f'Which is the new salary for job with id: {epilogi}?')
                new_salary_lbl.pack()
                new_salary = Entry(root)
                new_salary.pack()
                confirm_butt = Button(root, text = 'confirm', command = b)
                confirm_butt.pack()



            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')

            c = my_db.cursor()

            click = StringVar()
            click.set('epiloges')
            c.execute(f"SELECT id FROM job WHERE evaluator IN (SELECT username FROM evaluator LEFT JOIN company ON firm = afm LEFT JOIN manager ON manager.firm = afm WHERE managerUsername = '{onoma}')")
            c.execute("SELECT 'kostas';")
            j = []
            for i in c:
                j.append(i[0])

            ddb = OptionMenu(root, click, *j)
            question = Label(root, text = 'Which job needs a different slsary?')
            question.pack()
            ddb.pack()
            com_button = Button(root, text = 'commit', command = lambda:p(click.get()))
            com_button.pack()
            my_db.commit()
            c.close()
            my_db.close()

        def al_st_etair():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')

            c = my_db.cursor()
            if clicked.get() == "change com_phone":
                def kos():
                    c.execute(f"UPDATE company SET phone = '{new_phone}' WHERE afm IN (SELECT firm FROM manager WHERE '{onoma}' = managerUsername)")
                    new_phone.destroy()
                    new_phone_lbl.destroy()
                    ok_butt.destroy()
                new_phone_lbl = Label(root, text = "What is the new phone?")
                new_phone_lbl.pack()
                new_phone = Entry(root)
                new_phone.pack()
                ok_butt = Button(root, text = 'ok', command = kos)
                ok_butt.pack()
                
            
            if clicked.get() == 'change com_street':
                def k():
                    c.execute(f"UPDATE company SET street = '{new_street}' WHERE afm IN (SELECT firm FROM manager WHERE '{onoma}' = managerUsername)")
                    new_street.destroy()
                    new_street_lbl.destroy()
                    ok_butt1.destroy()
                new_street_lbl = Label(root, text = "What is the new street?")
                new_street_lbl.pack()
                new_street = Entry(root)
                new_street.pack()
                ok_butt1 = Button(root, text = 'ok', command = k)
                ok_butt1.pack()

            if clicked.get() == 'change_city':
                def ko():
                    c.execute(f"UPDATE company SET city = '{new_city}' WHERE afm IN (SELECT firm FROM manager WHERE '{onoma}' = managerUsername)")
                    new_city.destroy()
                    new_city_lbl.destroy()
                    ok_butt2.destroy()
                new_city_lbl = Label(root, text = 'What is the new city?')
                new_city_lbl.pack()
                new_city = Entry(root)
                new_city.pack()
                ok_butt2 = Button(root, text = 'ok', command = ko)
                ok_butt2.pack()

            if clicked.get() == 'change com_country':
                def kost():
                    c.execute(f"UPDATE company SET country = '{new_country}' WHERE afm IN (SELECT  firm FROM manager WHERE '{onoma}' = managerUsername)")
                    new_country.destroy()
                    new_country_lbl.destroy()
                    ok_butt3.destroy()
                new_country = Entry(root)
                new_country_lbl = Label(root, text = "What is the new country?")
                new_country_lbl.pack()
                new_country.pack()
                ok_butt3 = Button(root, text = 'ok', command = kost)
                ok_butt3.pack()

            my_db.commit()
            c.close()
            my_db.close()

        def allagi_stoixeiwn():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')

            c = my_db.cursor()

            if clicked2.get() == 'change personal email':
                def o():
                    c.execute(f"UPDATE user SET email = '{new_email}' WHERE username IN (SELECT managerUsername FROM manager WHERE managerUsername = '{onoma}')")
                    new_email.destroy()
                    new_email_lbl.destroy()
                    ok.destroy()
                new_email = Entry(root)
                new_email_lbl = Label(root, text = 'What is your new email?')
                new_email_lbl.pack()
                new_email.pack()
                ok = Button(root, text = 'ok', command = o)
                ok.pack()

            if clicked2.get() == 'change personal password':
                def op():
                    c.execute(f"SELECT password FROM user WHERE username IN (SELECT managerUsername FROM manager WHERE '{onoma}' = managerUsername)")
                    new_passwd.destroy()
                    new_passwd_lbl.destroy()
                    ok2.destroy()
                new_passwd = Entry(root)
                new_passwd_lbl = Label(root, text = 'What is your new password?')
                new_passwd_lbl.pack()
                new_passwd.pack()
                ok2 = Button(root, text = 'ok', command = op)
                ok2.pack()
            my_db.commit()
            c.close()
            my_db.close()

        def grades():
            def cl():
                grade_lbl.destroy()
                close_butt.destroy()
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')

            c = my_db.cursor()
            c.execute(f"SELECT EvId, job_id FROM evaluationresult WHERE job_id IN (SELECT id FROM job AS j INNER JOIN evaluator AS e ON j.evaluator = e.username INNER JOIN manager AS m on e.firm = m.firm WHERE managerUsername = '{onoma}')")
            c.execute("select 'kostas', 'kostas';")
            j = ''
            for i in c:
                j += i[0]+'\t'+i[1]+'\n'
            
            grade_lbl = Label(root, text = j)
            grade_lbl.pack()
            close_butt = Button(root, text = 'close',command = cl)
            close_butt.pack()
            my_db.close()
            c.close()        

        def show_average():
            my_db = mysql.connector.connect(host = 'localhost', 
            user = "root", 
            password = '11111111', 
            database = 'evaluating')

            c = my_db.cursor()
            onoma_eval = Entry(root)
            c.execute("SELECT ")



        allagi_stoi_etair = OptionMenu(root, clicked,
        "change com_phone", "change com_street","change_city", "change com_country")
        allagi_stoi_etair.pack()
        epibebaiwsi = Button(root, text = "commit", command = al_st_etair)
        epibebaiwsi.pack()
        allagi_proswpikwn_stoixeiwn = OptionMenu(root, clicked2, 
        "change personal email", "change personal password")
        allagi_proswpikwn_stoixeiwn.pack()
        epibebaiwsi2 = Button(root, text = "commit", command = allagi_stoixeiwn)
        epibebaiwsi2.pack()
        sal_change = Button(root, text = "Change salaries", command = al_misthou)
        sal_change.pack()
        mo_butt = Button(root, text = "average grade", command = show_average)
        
        check_perm_grades = Button(root, text = 'Permanent grades', command = grades)
        check_perm_grades.pack()
    manager_first_page()
    root.mainloop()
