from DBTable_Sample import InsertData


class Car:
    def __init__(self,colour,model,prize):
        self.colour = colour
        self.model = model
        self.prize = prize


cardetaillist= InsertData.readTheText()
print(cardetaillist)
tableName= 'carDetails'
listOfColumns= ['CarColor', 'CarPrize', 'CarModel']
listOfUserDetailsDict = cardetaillist
query,insertData = InsertData.createSqlQuery(tableName,listOfColumns,listOfUserDetailsDict)
print(query)
print(insertData)

