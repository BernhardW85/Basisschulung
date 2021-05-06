import mysql.connector

mydb = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n"
)

print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE dbBWL")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

mydb.close()

# danach normaler python code
