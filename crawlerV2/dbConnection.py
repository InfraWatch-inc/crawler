import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="infrawatch"
)



cursor = connection.cursor()
