
class Address:
    
    def __init__(self,houseNum,add1,add2,country,state,city,postalCode):
        self.houseNum = houseNum
        self.address1 = add1
        self.address2 = add2
        self.country = country
        self.country.encode('UTF-8')
        self.state = state
        self.city = city
        self.postalCode = postalCode

    def __str__(self):        
        return ("\"#"+str(self.houseNum)+ "," + str(self.address1)+ "\"," +str(self.address2) +","+self.city+","+self.state+","+self.country+","+str(self.postalCode))
    
    def __dir__(self):
        return(["address1","address2"])