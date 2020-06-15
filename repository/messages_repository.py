class MessageRepository():

    def findById(self, database, user_id):
        data = []
        row = {}
        
        SQL_SELECT = f"SELECT m.`id`, m.`content`, u.`name`, m.`time`, m.`user_id`, m.`type` FROM `Messages` as m INNER JOIN Users as u ON user_id = u.id WHERE user_id = {user_id} ORDER BY m.`time`"
        for item in database.findAll(SQL_SELECT):
            row["id"] = item[0]
            row["content"] = item[1]
            row["name"] = item[2]
            row["time"] = item[3]
            row["user_id"] = item[4]
            row["type"] = item[5]
            data.append(row)
            row = {}
        return data
        

