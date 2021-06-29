import cx_Oracle
try:
    con = cx_Oracle.connect('hr/hr@localhost')
    print("Data Base Version : ",con.version)
    cursor=con.cursor()
    cursor.execute("create table manager(id int,name varchar(15))")
    cursor.execute("create table student(id int,name varchar(15))")
    print("Manager Table created successfully")
    print("Student Table created successfully")
    '''cursor.execute("insert into manager values(1,'Rubesh')")
    cursor.execute("insert into manager values(2,'Arun')")
    cursor.execute("insert into student values(3,'Rahul')")
    cursor.execute("insert into student values(4,'Deepak')")'''
    print("Values inserted in both tables")
    cursor.execute("create table employee(id int,name varchar(15))")
    print("Employerr Table created successfully")
    '''cursor.execute("insert into employee values(11,'Rajesh')")
    cursor.execute("insert into employee values(12,'Kiran')")
    cursor.execute("insert into employee values(13,'Ashok')")
    cursor.execute("insert into employee values(14,'Dilip')")'''
    print("Values inserted into employee table successfully")
    print("Printing employee table using for loop.....")
    cursor.execute("select * from employee")
    rows=cursor.fetchall()
    j=0
    for i in rows:
        print("Row ",(j+1),": ",i)
        j+=1
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
con.close()
