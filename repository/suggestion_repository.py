class SuggestionRepository():

    def findAll(self, database):
        data = []
        row = {}
        
        SQL_SELECT = "SELECT * FROM `Suggestions` ORDER BY RAND()"
        for item in database.findAll(SQL_SELECT):
            row["id"] = item[0]
            row["title"] = item[1]
            row["type"] = item[2]
            row["description"] = item[3]
            row["url"] = item[4]
            row["image_url"] = item[5]
            data.append(row)
            row = {}

        
        return data
        
