import mysql.connector

conn = mysql.connector.connect(username='root', password='MySQLPs2312Project',host='localhost',database='Crime_Tracker',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()