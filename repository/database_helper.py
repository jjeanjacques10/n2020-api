import mysql.connector

class DatabaseHelper():
    def connect_database(self):
        mydb = mysql.connector.connect(
            host="tenneducation.com.br",
            user="tenned93_jean",
            passwd="n2020bot",
            database="tenned93_n2020",
            auth_plugin='mysql_native_password'
        )
        return mydb

    def findAll(self, sql):
        mydb = self.connect_database()
        mycursor = mydb.cursor()

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        return myresult
 
