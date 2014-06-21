
from builtins import type

class Generator :
    
    def getRandomNumber(self,maxNum):
        import math,random
        return(math.ceil(random.triangular(1,maxNum)))
    
    def create_type(self,name, dic):
        return type(name, (object,), dic)
    
    def getRandomString(self,length):
        import random, string,math
        i = 0
        s = ''
        length=math.ceil(random.triangular(1,length))
        while (i<length) :
            s+=random.choice(string.ascii_letters)
            i+=1
        return (s.upper())
    
    def getRandomStringsList(self,noOfStrings,maxLength):
        import random, math
        i=0
        lst = []
        while(i<noOfStrings) :
            curLen = math.ceil(random.triangular(1,maxLength))
            lst.append(self.getRandomString(curLen))
            i+=1;
        return(lst)
    
    def getRandomGender(self) :
        import  random
        gender = random.choice(["M","F"])
        return(gender)
    
    def getRandomPrefix(self,gender,age) :
        import  random
        prefix = ""
        if(gender == "F" and age>=20) :
            prefix = random.choice(["Dr.","Ms.","Mrs."])
        elif (gender=="F"):
            prefix = random.choice(["Dr.","Ms."])
        else:
            prefix = random.choice(["Dr.","Mr."])
        return(prefix)
    
    def getRandomBirthDate(self,start,end,format):
        
        import datetime,time,random,math
        
        epoch = datetime.datetime(1970,1,1,0,0,0) #epoch datetime
        sdt = datetime.datetime(*(time.strptime(start,format)[0:6]))
        edt = datetime.datetime(*(time.strptime(end,format)[0:6]))
        
        ddt = (sdt-epoch)
        sts = ddt.days*24*3600 + ddt.seconds
        ets = edt.timestamp()
        
        rts = math.ceil(random.triangular(sts,ets))
        
        if(rts<0) :
            return(sdt + datetime.timedelta(seconds=((-1)*rts)))
        else :
            return(epoch + datetime.timedelta(seconds=rts))
    
    
    def getAgeFromBirthDate(self,dob,dod):
        from datetime import date
        if(dod==0):
            today = date.today()
            return(today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)))
        else :
            return(dod.year - dob.year -((dod.month, dod.day) < (dod.month, dod.day)))
    
    def getRandomDeathDate(self,birthdate):
        import datetime,random,math,time
        epoch = datetime.datetime(1970,1,1,0,0,0) #epoch datetime
        sts = None
        
        if(birthdate < epoch):
            ddt = (birthdate-epoch)
            sts = ddt.days*24*3600 + ddt.seconds
        else:
            sts = birthdate.timestamp() 
        
        ets = time.time()
        rts = math.ceil(random.triangular(sts,ets))
        
        if(rts<0) :
            return(birthdate + datetime.timedelta(seconds=((-1)*rts)))
        else :
            return(epoch + datetime.timedelta(seconds=rts))
        
        
    def getRandomUuid(self):
        import pymysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs') #else connect to default mysqldb
        cur = conn.cursor()
        cur.execute("SELECT uuid() FROM dual")
        r = ""
        for row in cur:
            r = row[0]
        cur.close()
        conn.close()
        return r
     
    def getRandomCountry(self):
        import pymysql
        conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')
        cur = conn.cursor()
        cur.execute("SELECT country FROM city_state_country ORDER BY RAND() LIMIT 1")
        r = ""
        for row in cur:
            r = row[0]
        return r
    
    def getRandomState(self,country):
        import pymysql
        conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')
        cur = conn.cursor()
        cur.execute("SELECT state FROM city_state_country where country like '"+country+"' ORDER BY RAND() LIMIT 1")
        r = ""
        for row in cur:
            r = row[0]
        return r
    
    def getRandomCity(self,state):
        import pymysql
        conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')
        cur = conn.cursor()
        cur.execute("SELECT city FROM city_state_country where state like '"+state+"' ORDER BY RAND() LIMIT 1")
        r = ""
        for row in cur:
            r = row[0]
        return r
    
    def getRandomPostalCode(self,start,end):
        import math,random
        return math.ceil(random.triangular(start,end))
    
    def getRandomConceptId(self):
        import pymysql,math,random
        conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')
        cur = conn.cursor()
        cur.execute("SELECT concept_id FROM concept ORDER BY RAND() LIMIT 1")
        for row in cur:
            return row[0]
        return math.ceil(random.triangular(1,1200)) #because 1200 concepts are only available in order sequence in db
    
    def addRandomSpacesToString(self,maxNumSpaces,str):
        import random,math
        numSpaces=math.ceil(random.triangular(1,maxNumSpaces))
        i = 0
        while(i<numSpaces):
            pos = math.ceil(random.triangular(1,len(str)))
            str = str[:pos] + " " + str[pos:]
            i+=1
        return str    
        
    def getRandomAddress(self,houseNumLimit,address1LenLimit,address2LenLimit,postalCodeStart,postalCodeEnd):
        import random, math
        address1 = self.getRandomString(address1LenLimit)
        address2 = self.getRandomString(address2LenLimit)
        houseNum = math.ceil(random.triangular(1,houseNumLimit))
        country = self.getRandomCountry()
        state = self.getRandomState(country)
        city = self.getRandomCity(state)
        postalCode = self.getRandomPostalCode(postalCodeStart,postalCodeEnd)
        address1 = self.addRandomSpacesToString(self.getRandomNumber(10),address1)
        address2 = self.addRandomSpacesToString(self.getRandomNumber(10),address2)
        return(self.create_type('address',{"houseNum" : houseNum, "add1" : address1, "add2" : address2, "country" : country,"state":state,"city":city,"postalCode":postalCode}))
    
    def getRandomGeoLatitude(self,startLat,endLat):
        import random, math
        d = math.ceil(random.triangular(1,10))
        t = 1/d
        return(math.ceil(random.triangular(startLat,endLat))+t)
        
    def getRandomGeoLongitude(self,startLong,endLong):
        import random, math
        d = math.ceil(random.triangular(1,10))
        t = 1/d
        return(math.ceil(random.triangular(startLong,endLong)) + t)
        
    