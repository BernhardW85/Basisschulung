import mysql.connector

mydb = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n",
    database="sql11404167"
)
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customerBWL"
mycursor.execute(sql)
mycursor.execute("CREATE TABLE customerBWL (name VARCHAR(255), adress VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for tables in mycursor:
    print(tables)

mycursor.execute("ALTER TABLE customerBWL ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO customerBWL (name, adress) VALUES (%s, %s)"
#values = ("Bernhard", "Straße 65")
values = [("Bernhard", "Straße 65"), ("Max", "Weg 10")]
#mycursor.execute(sql, values)
mycursor.executemany(sql, values)

mydb.commit()

print(mycursor.rowcount, "... Anzahl an Datensätzen")
print("ID: ", mycursor.lastrowid)

sql = "SELECT * FROM customerBWL WHERE adress = 'Straße 65'"
mycursor.execute(sql)
# myresult = mycursor.fetchone()
# print(myresult)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)

mydb.close()