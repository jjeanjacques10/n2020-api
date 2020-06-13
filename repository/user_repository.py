from models.user_model import UserModel

class UserRepository():

    def insert(self):   
        print("aasdas")

    def login(self, database, email, password):
        row = {}
        data = []
        user = (email, password)
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
