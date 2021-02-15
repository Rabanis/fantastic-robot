import mysql.connector

def is_emoployee(uname):
    my_db = mysql.connector.connect(host = 'localhost', user = 'root', password = '11111111', database = 'evaluating')
    curs = my_db.cursor()
    curs.execute(f"SELECT username FROM employee WHERE username = '{uname}'")
    for i in curs:
        if i[0] == uname:
            return uname
        else:
            return False

def is_manager(uname):
    my_db = mysql.connector.connect(host = 'localhost', user = 'root', password = '11111111', database = 'evaluating')
    curs = my_db.cursor()
    curs.execute(f'SELECT managerUsername FROM manager WHERE managerUsername = "{uname}"')
    for i in curs:
        if i[0] == uname:
            return uname
        else:
            return False

def is_evaluator(uname):
    my_db = mysql.connector.connect(host = 'localhost', user = 'root', password = '11111111', database = 'evaluating')
    curs = my_db.cursor()
    curs.execute(f'SELECT username FROM evaluator WHERE username = "{uname}"')
    for i in curs:
        if i[0] == uname:
            return uname
        else:
            return False

def is_admin(uname):

    my_db = mysql.connector.connect(host = 'localhost', user = 'root', password = '11111111', database = 'evaluating')
    curs = my_db.cursor()
    curs.execute(f'SELECT admin_username FROM admin WHERE admin_username = "{uname}"')
    for i in curs:
        if i[0] == uname:
            return uname
        else:
            return False
