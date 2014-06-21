
class Name:
    
    def __init__(self,givenName,middleName,familyName):
        self.givenName = givenName
        self.middleName = middleName
        self.familyName = familyName
        
    def __str__(self):
        return(self.givenName + "," + self.middleName + "," +self.familyName)
    
    def __dir__(self):
        return(["givenName","middleName","familyName"])    