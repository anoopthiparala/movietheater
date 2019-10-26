import cx_Oracle
if __name__=="__main__":
    dsnt = cx_Oracle.makedsn("localhost", "1521", service_name = "orcl")
    conn = cx_Oracle.connect(user="system", password="Anoop1998", dsn=dsnt)
    c = conn.cursor()
    c.execute("alter session set container=orclpdb")
    #scheme is anoop
    c.execute("CREATE TABLE USERS (ID INT PRIMARY KEY, PASSWORD VARCHAR2(20))")
    c.execute("CREATE TABLE ADMINS (ID INT PRIMARY KEY, PASSWORD VARCHAR2(20))")
    c.execute("CREATE TABLE THEATERS (ID INT PRIMARY KEY, NAME VARCHAR2(20))")
    c.execute("CREATE TABLE MOVIES (MOVIE_ID INT PRIMARY KEY, NAME VARCHAR2(20), PRICE INT NOT NULL, THEATER_ID INT, "
              "FOREIGN KEY (THEATER_ID) REFERENCES THEATER (ID))")
    c.execute("commit")
