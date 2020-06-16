from models.user_model import UserModel

class UserRepository():

    def insert(self, database, user):   
        row = (user["name"], user["photoUrl"], user["phone"], user["email"],  user["password"])

        SQL_INSERT = "INSERT INTO `Users`(`name`, `photo_url`, `phone`, `email`, `password`) VALUES (%s,%s,%s,%s,%s)"
        result = database.insertRow(SQL_INSERT, row)
        return result

    def login(self, database, user):
        row = {}
        data = []
        user = (user.email, user.password)
        SQL_SELECT = "SELECT * FROM `Users` WHERE email = %s and password = %s"
        result = database.findByEmailPassword(SQL_SELECT, user)
        if(len(result) > 0):
            for item in result:
                row["id"] = item[0]
                row["photoUrl"] = item[1]
                row["name"] = item[2]
                row["phone"] = item[3]
                row["email"] = item[4]
                row["password"] = item[5]
                data = row
                row = []
            return data
        else:
            return []
