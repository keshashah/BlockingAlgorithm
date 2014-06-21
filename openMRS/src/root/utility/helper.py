
from root.utility.generator import Generator
from root.models.patient import Patient
from root.models.address import Address
from root.models.name import Name

def getRandomPatientsData(numPatients, numPatientsWithDeath, numDirtyPatients):
    import math
    if(numPatients < numPatientsWithDeath):
        print("Number of deaths cannot be greater than number of patients")
        return
    elif (numPatients <= 0):
        print("Number of patients cannot be equal to or less than zero")
        return 
    print("Generating random records...")    
    numPatientsWithoutDeath = numPatients - numPatientsWithDeath
    numPatientsWithoutDeath = numPatientsWithoutDeath - math.ceil(numDirtyPatients / 2)
    numPatientsWithDeath = numPatientsWithDeath - math.ceil(numDirtyPatients / 2 - 1)
    
    i = 0
    g = Generator()
    patients = []
    while i < numPatientsWithoutDeath : 
        
        gender = g.getRandomGender()
        birthdate = g.getRandomBirthDate("1/1/1940 6:00 AM", "4/5/2014 11:59 PM", '%d/%m/%Y %I:%M %p')
        uuid = g.getRandomUuid()
        latitude = g.getRandomGeoLatitude(-90, 90)
        longitude = g.getRandomGeoLongitude(-180, 180)
        dead = 0
        deathDate = None
        causeOfDeath = None
        
        age = g.getAgeFromBirthDate(birthdate, 0)
        
        givenName = g.getRandomString(g.getRandomNumber(30))
        middleName = g.getRandomString(g.getRandomNumber(30))
        familyName = g.getRandomString(g.getRandomNumber(30))
        name = Name(givenName, middleName, familyName)
        
        address = g.getRandomAddress(1000, 100, 100,100000,1000000)
        address = Address(address.houseNum, address.add1, address.add2, address.country,address.state,address.city,address.postalCode)
        
        p = Patient(uuid, gender, birthdate, age, dead, deathDate, causeOfDeath, latitude, longitude)
        p.setName(name)
        p.setAddress(address)
        patients.append(p)
        i += 1
    
    i = 0
    
    while i < numPatientsWithDeath :
    
        gender = g.getRandomGender()
        birthdate = g.getRandomBirthDate("1/1/1940 6:00 AM", "4/5/2014 11:59 PM", '%d/%m/%Y %I:%M %p')
        uuid = g.getRandomUuid()
        latitude = g.getRandomGeoLatitude(-90, 90)
        longitude = g.getRandomGeoLongitude(-180, 180)
        
        dead = 1
        deathDate = g.getRandomDeathDate(birthdate)
        causeOfDeath = g.getRandomString(g.getRandomNumber(100))
        causeOfDeath = g.addRandomSpacesToString(g.getRandomNumber(10), causeOfDeath)

        age = g.getAgeFromBirthDate(birthdate, deathDate)
        
        givenName = g.getRandomString(g.getRandomNumber(30))
        middleName = g.getRandomString(g.getRandomNumber(30))
        familyName = g.getRandomString(g.getRandomNumber(30))
        name = Name(givenName, middleName, familyName)
        
        address = g.getRandomAddress(1000, 100, 100,100000,1000000)
        address = Address(address.houseNum, address.add1, address.add2, address.country,address.state,address.city,address.postalCode)
        
        p = Patient(uuid, gender, birthdate, age, dead, deathDate, causeOfDeath, latitude, longitude)
        p.setName(name)
        p.setAddress(address)
        
        patients.append(p)
        i += 1
    print("Random records generated successfully.")
    
    return generateDirtyPatientsData(patients, numDirtyPatients, g)
       

def generateDirtyPatientsData(patients, numDirtyPatients, generator):
    
    import math, random, copy, string
    i = 0
    while(i < numDirtyPatients):
        
        # get a random patient
        d = math.ceil(random.triangular(0, len(patients) - 1))
        rand_p = patients[d] 
        
        attr = (dir(rand_p)[math.ceil(random.triangular(0, len(dir(rand_p)) - 1))])
        
        # get a random attribute
        rand_attr = getattr(rand_p, attr)
        
        # create a dirty patient record
        new_p = copy.deepcopy(rand_p)
        
        if attr == "name":
            name_dir = dir(new_p.name)
            name_attr = name_dir[math.ceil(random.triangular(0, len(name_dir) - 1))]
            name_val = getattr(new_p.name, name_attr)            
            name_val_len = len(name_val)
            num_chars_to_permute = math.ceil(random.triangular(0, name_val_len))
            j = 0
            while(j < num_chars_to_permute):
                r = random.choice(string.ascii_letters)
                k = math.ceil(random.triangular(1, name_val_len - 1))
                name_val = name_val[:k] + r + name_val[k + 1:]
                j += 1
            setattr(new_p.name, name_attr, name_val)
        
        elif attr == "address":
            addr_dir = dir(new_p.address)
            addr_attr = addr_dir[math.ceil(random.triangular(0, len(name_dir) - 1))]
            addr_val = getattr(new_p.address, addr_attr)            
            addr_val_len = len(addr_val)
            num_chars_to_permute = math.ceil(random.triangular(0, addr_val_len))
            j = 0
            while(j < num_chars_to_permute):
                r = random.choice(string.ascii_letters)
                k = math.ceil(random.triangular(1, addr_val_len - 1))
                addr_val = addr_val[:k] + r + addr_val[k + 1:]
                j += 1
            setattr(new_p.address, addr_attr, addr_val)
            
        elif attr == "age":
            age_attr = "age"
            age_val = getattr(new_p, age_attr)
            start = age_val - 5
            if(age_val < 5) :
                start = 0            
            end = age_val + 5
            new_age = math.ceil(random.triangular(start, end))
            setattr(new_p, age_attr, new_age)
        
        elif attr == "latitude":
            lat_attr = "latitude"
            lat_val = getattr(new_p, lat_attr)
            start = lat_val - 5
            end = lat_val + 5
            if(lat_val < -85) :
                start = -90 
            elif (lat_val > 85) :
                end = 90               
            new_lat = math.ceil(random.triangular(start, end))
            setattr(new_p, lat_attr, new_lat)
            
        elif attr == "longitude":
            long_attr = "longitude"
            long_val = getattr(new_p, long_attr)
            start = long_val - 5
            end = long_val + 5
            if(long_val < -175) :
                start = -180 
            elif (long_val > 175) :
                end = 180               
            new_long = math.ceil(random.triangular(start, end))
            setattr(new_p, long_attr, new_long)
            
        elif attr == "causeOfDeath":
            cod_attr = "causeOfDeath"
            cod_val = getattr(new_p, cod_attr)
            if(cod_val != None):            
                cod_val_len = len(cod_val)
                num_chars_to_permute = math.ceil(random.triangular(0, cod_val_len))
                j = 0
                while(j < num_chars_to_permute):
                    r = random.choice(string.ascii_letters)
                    k = math.ceil(random.triangular(1, cod_val_len - 1))
                    cod_val = cod_val[:k] + r + cod_val[k + 1:]
                    j += 1
                setattr(new_p, cod_attr, cod_val)         
        i += 1
        setattr(new_p,"uuid",generator.getRandomUuid())
        patients.append(new_p)
        
    return patients
    

def writeToFileHeader(file, header):
    import codecs
    f = codecs.open(file, 'w', "utf-8")
    f.write(header)
    f.write("\n")
    f.close()    

def writeToFilePatients(file, patients):
    import codecs
    f = codecs.open(file, 'a', "utf-8")
    print("Writing generated records to file...")
    i = 0
    while(i < len(patients)):
        patient = str(patients[i])
        f.write(patient)
        f.write(",")
        name = str(patients[i].name) 
        f.write(name)
        f.write(",")
        address = str(patients[i].address)
        address.encode(encoding='utf_8', errors='strict')
        f.write(address)
        f.write("\n")
        i += 1
    f.close()
    print("Records written to file successfully.")

