import mysql.connector

class DatabaseHelper():
    def connect_database(self):
        mydb = mysql.connector.connect(
            host="",
            user="",
            passwd="",
            database="",
            auth_plugin='mysql_native_password'
        )
        return mydb

    def findAll(self, sql):
        mydb = self.connect_database()
        mycursor = mydb.cursor()

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        return myresult
 
    def findById(self, sql, id):
        pass

    def findByEmailPassword(self, sql, data):
        mydb = self.connect_database()
        mycursor = mydb.cursor()

        mycursor.execute(sql, data)

        myresult = mycursor.fetchall()
        return myresult


    def insertRow(self, sql, data):
        mydb = self.connect_database()
        mycursor = mydb.cursor()

        mycursor.execute(sql, data)

        mydb.commit()

        return mycursor.rowcount
