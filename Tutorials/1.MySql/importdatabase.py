import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='bibin', passwd='1234', database='tutorial')
mycursor = mydb.cursor()
mycursor.execute("insert into student values('vishnu','icet')")
mycursor.execute("select * from student")
result = mycursor.fetchall()
for i in result:
    print(i)
