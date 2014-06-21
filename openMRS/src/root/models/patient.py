
class Patient :
    '''
    Patient Class
    '''
    
    def __init__(self,uuid, gender,birthDate,age,dead,deathDate,causeOfDeath,latitude,longitude):
        self.uuid = uuid
        self.gender = gender
        self.birthDate = birthDate
        self.age = age
        self.dead = dead    
        self.deathDate = deathDate
        self.causeOfDeath = causeOfDeath
        self.latitude = latitude
        self.longitude = longitude
#       self.birthdateEstimated = birthdateEstimated
        
    def setAddress(self,address):
        self.address = address
        
    def setName(self,name):
        self.name = name   
        
    def __str__(self):
        #return(self.uuid +"," +self.name + "," +self.gender + ","+self.birthdate.strftime('%m/%d/%Y') + ", "+self.address)
        if(self.deathDate==None):
            return(self.uuid + "," +self.gender + ","+ str(self.age) +","+self.birthDate.strftime('%m/%d/%Y')+","+str(self.dead)+","+str(self.deathDate)+","+str(self.causeOfDeath)+","+str(self.latitude)+","+str(self.longitude))
        else :
            return(self.uuid + "," +self.gender + ","+ str(self.age) +","+self.birthDate.strftime('%m/%d/%Y')+","+str(self.dead)+","+self.deathDate.strftime('%m/%d/%Y')+","+self.causeOfDeath+","+str(self.latitude)+","+str(self.longitude))
        
    def __dir__(self):
        return (['address', 'age', 'causeOfDeath', 'latitude', 'longitude', 'name'])