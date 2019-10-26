import cx_Oracle
def book(uid):
    print("Select the theater from the following:")
    c.execute("SELECT * FROM ANOOP.THEATERS")
    print("ID\tNAME")
    for r in c:
        print(r[0], "\t", r[1])
    tid=int(input("Enter theater ID:"))
    c.execute("SELECT * FROM ANOOP.MOVIES WHERE THEATER_ID={}".format(tid))
    print("ID\tNAME\t\tPRICE")
    for r in c:
        print(r[0], "\t", r[1], "\t", r[2])
    mid=int(input("Enter movie ID:"))
    n=int(input("Enter number of tickets:"))
    c.execute("SELECT PRICE FROM ANOOP.MOVIES WHERE MOVIE_ID={}".format(mid))
    for res in c:
        c41=int(res[0])
    cost=n*c41
    c.execute("SELECT NAME FROM ANOOP.THEATERS WHERE ID={}".format(tid))
    for res in c:
        tname=res[0]
    c.execute("SELECT NAME FROM ANOOP.MOVIES WHERE MOVIE_ID={} AND THEATER_ID={}".format(mid,tid))
    for res in c:
        mname=res[0]
    print("----------------------------------------------------------------------------------")
    print("************************************TICKET****************************************")
    print("----------------------------------------------------------------------------------")
    print("USER ID: ", uid)
    print("THEATER ID: ", tid)
    print("THEATER NAME: ", tname)
    print("MOVIE ID: ", mid)
    print("MOVIE NAME: ", mname)
    print("NUMBER OF TICKETS: ", n)
    print("TOTAL COST: ", cost)
    print("----------------------------------------------------------------------------------")
def view():
    while (True):
        print("What do you want to do:")
        print("1.VIEW USERS")
        print("2.VIEW ADMINS")
        print("3.VIEW THEATERS")
        print("4.VIEW MOVIES")
        print("Enter any other number to exit")
        ch = int(input("Enter your option:"))
        if (ch == 1):
            c.execute("SELECT * FROM ANOOP.USERS")
            columns = c.description
            result = []
            for value in c.fetchall():
                tmp = {}
                for (index, column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
            for i in result:
                print(i)
        elif (ch == 2):
            c.execute("SELECT * FROM ANOOP.ADMINS")
            columns = c.description
            result = []
            for value in c.fetchall():
                tmp = {}
                for (index, column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
            for i in result:
                print(i)
        elif (ch == 3):
            c.execute("SELECT * FROM ANOOP.THEATERS")
            columns = c.description
            result = []
            for value in c.fetchall():
                tmp = {}
                for (index, column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
            for i in result:
                print(i)
        elif (ch == 4):
            c.execute("SELECT * FROM ANOOP.MOVIES")
            columns = c.description
            result = []
            for value in c.fetchall():
                tmp = {}
                for (index, column) in enumerate(value):
                    tmp[columns[index][0]] = column
                result.append(tmp)
            for i in result:
                print(i)
        else:
            break;
def add():
    while (True):
        print("What do you want to do:")
        print("1.ADD USER")
        print("2.ADD ADMIN")
        print("3.ADD THEATER")
        print("4.ADD MOVIE")
        print("Enter any other number to exit")
        ch = int(input("Enter your option:"))
        if (ch == 1):
            c.execute("INSERT INTO ANOOP.USERS VALUES({},'{}')".format(int(input("Enter user ID:")),
                                                                       input("Enter password:")))
            c.execute("commit")
        elif (ch == 2):
            c.execute("INSERT INTO ANOOP.ADMINS VALUES({},'{}')".format(int(input("Enter admin ID:")),
                                                                        input("Enter password:")))
            c.execute("commit")
        elif (ch == 3):
            c.execute("INSERT INTO ANOOP.THEATERS VALUES({},'{}')".format(int(input("Enter theater ID:")),
                                                                  input("Enter theater name:")))
            c.execute("commit")
        elif (ch == 4):
            c.execute("INSERT INTO ANOOP.MOVIES VALUES({},'{}',{},{})".format(int(input("Enter movie ID:")),
                                                                      input("Enter movie name:"),
                                                                      int(input("Enter price of ticket:")),
                                                                       int(input("Enter theater ID:"))))
            c.execute("commit")
        else:
            break;
def remove():
    while (True):
        print("What do you want to do:")
        print("1.REMOVE USER")
        print("2.REMOVE ADMIN")
        print("3.REMOVE THEATER")
        print("4.REMOVE MOVIE")
        print("Enter any other number to exit")
        ch = int(input("Enter your option:"))
        if (ch == 1):
            c.execute("DELETE FROM ANOOP.USERS WHERE ID={}".format(int(input("Enter user ID:"))))
            c.execute("commit")
        elif (ch == 2):
            c.execute("DELETE FROM ANOOP.ADMINS WHERE ID={}".format(int(input("Enter admin ID:"))))
            c.execute("commit")
        elif (ch == 3):
            c.execute("DELETE FROM ANOOP.THEATERS WHERE ID={}".format(int(input("Enter theater ID:"))))
            c.execute("commit")
        elif (ch == 4):
            c.execute("DELETE FROM ANOOP.MOVIES WHERE ID={}".format(int(input("Enter movie ID:"))))
            c.execute("commit")
        else:
            break;
def update():
    while (True):
        print("What do you want to do:")
        print("1.UPDATE USER")
        print("2.UPDATE ADMIN")
        print("3.UPDATE THEATER")
        print("4.UPDATE MOVIE PRICE")
        print("Enter any other number to exit")
        ch = int(input("Enter your option:"))
        if (ch == 1):
            c.execute("UPDATE ANOOP.USERS SET PASSWORD={} WHERE ID={}".format(input("Enter new password:"),
                                                                        int(input("Enter user ID:"))))
            c.execute("commit")
        elif (ch == 2):
            c.execute("UPDATE ANOOP.ADMINS SET PASSWORD={} WHERE ID={}".format(input("Enter new password:"),
                                                                        int(input("Enter admin ID:"))))
            c.execute("commit")
        elif (ch == 3):
            c.execute("UPDATE ANOOP.THEATERS SET NAME='{}' WHERE ID={}".format(input("Enter new name:"),
                                                                        int(input("Enter theater ID:"))))
            c.execute("commit")
        elif (ch == 4):
            c.execute("UPDATE ANOOP.MOVIES SET PRICE={} WHERE ID={}".format(int(input("Enter new price:")),
                                                                       int(input("Enter movie ID:"))))
            c.execute("commit")
        else:
            break;
def user():
    while (True):
        id=int(input("Enter user ID:"))
        c.execute("SELECT * FROM ANOOP.USERS WHERE ID={} AND PASSWORD='{}'".format(id, input("Enter password:")))
        row = c.fetchone()
        if(row!=None):
            print("What do you want to do:")
            print("1.BOOK A TICKET")
            print("Enter any other number to exit")
            ch = int(input("Enter your option:"))
            if (ch == 1):
                book(id)
            else:
                break;
        else:
            break;
def admin():
    while (True):
        id = int(input("Enter admin ID:"))
        pas=input("Enter password:")
        c.execute("SELECT * FROM ANOOP.ADMINS WHERE ID={} AND PASSWORD='{}'".format(id,pas))
        row = c.fetchone()
        if (row != None):
            print("What do you want to do:")
            print("1.ADD")
            print("2.REMOVE")
            print("3.UPDATE")
            print("4.VIEW")
            print("Enter any other number to exit")
            ch = int(input("Enter your option:"))
            if (ch == 1):
                add()
            elif (ch == 2):
                remove()
            elif (ch == 3):
                update()
            elif (ch == 4):
                view()
            else:
                break;
        else:
            break;

if __name__=="__main__":
    dsnt = cx_Oracle.makedsn("localhost", "1521", service_name = "orcl")
    conn = cx_Oracle.connect(user="system", password="Anoop1998", dsn=dsnt)
    c = conn.cursor()
    c.execute("alter session set container=orclpdb")
    while(True):
        print("Are you a :")
        print("1.USER")
        print("2.ADMIN")
        print("Enter any other number to exit")
        ch = int(input("Enter your option:"))
        if(ch==1):
            user()
        elif(ch==2):
            admin()
        else:
            break;

