class InsertData:
    @staticmethod
    def createSqlQuery(tableName,listOfColumns,listOfUserDetailsDict):
        query = "INSERT INTO {} ({},{},{}) VALUES (%s,%s,%s)".format(tableName,listOfColumns[0],listOfColumns[1],listOfColumns[2])
        valuseToInsert = []
        for userDetailsDict in listOfUserDetailsDict:
            if userDetailsDict is not None:
                if userDetailsDict[listOfColumns[0]] is not None:
                    CarColor = userDetailsDict[listOfColumns[0]]
                if userDetailsDict[listOfColumns[1]] is not None:
                    CarPrize = userDetailsDict[listOfColumns[1]]
                if userDetailsDict[listOfColumns[2]] is not None:
                    CarModel = userDetailsDict[listOfColumns[2]]
                valuseToInsert.append((CarColor,CarPrize,CarModel))
        return query,valuseToInsert

    @staticmethod
    def readTheText():
        cardel = ['CarColor', 'CarPrize', 'CarModel']
        cardetaillist = []
        with open("text.txt", 'r') as carDetails:
            for cardetail in carDetails:
                # print(cardetail,end=" ")
                model = cardetail.split(',')
                cardetaillist.append({cardel[0]: model[0], cardel[1]: model[1], cardel[2]: model[2].strip()})
        return cardetaillist