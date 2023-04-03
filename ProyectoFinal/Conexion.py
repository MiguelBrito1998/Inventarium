import pymysql

conection=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="project"
)
cursor=conection.cursor()

