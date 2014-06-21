from root.utility.generator import Generator
#person table

def insertScript(tableName, person, idStart) :
    
    g = Generator()
    qStr = 'INSERT INTO `'+tableName+"` "
    qStr+= 'VALUES ('

# Format for person
#INSERT INTO `person` VALUES (14,'M','06/08/1973',1,0,NULL,NULL,1,'2006-01-18 00:00:00',NULL,NULL,0,NULL,NULL,NULL,'dd5536fz-1691-11df-97a5-7038c432aabf',0);
    
    if(tableName=='person'):
        qStr+=str(idStart)+","
        qStr+="'"+person.gender+"',"
        qStr+="'"+person.birthDate.strftime('%Y-%m-%d')+"',"
        qStr+="0,"
        if(person.dead):
            qStr+=str(person.dead)+","
            qStr+="'"+person.deathDate.strftime('%Y-%m-%d')+"',"
            qStr+=str(g.getRandomConceptId())+","
        else:
            qStr+="0,"
            qStr+="NULL,"
            qStr+="NULL,"
        qStr+="1,"
        qStr+="'2014-01-21"+" 00:00:00',"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="0,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="'"+person.uuid+"',"
        qStr+="0);"

# Format for person_name       
# INSERT INTO `person_name` VALUES (13,0,13,NULL,'Jarus','Agemba',NULL,'Rapondi',NULL,NULL,NULL,1,'2006-01-18 00:00:00',0,NULL,NULL,NULL,NULL,NULL,'de814b7c-1691-11df-97a5-7038c432aabf')

    elif(tableName=='person_name'):
        personName = person.name 
        qStr+=str(idStart)+","
        qStr+="1,"
        qStr+=str(idStart)+","
        qStr+="NULL,"
        qStr+="'"+personName.givenName+"',"
        qStr+="'"+personName.middleName+"',"
        qStr+="NULL,"
        qStr+="'"+personName.familyName+"',"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="1,"
        qStr+="'2014-01-21"+" 00:00:00',"
        qStr+="0,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="'"+person.uuid+"');"
    
#Format for personAddress
#INSERT INTO `person_address` VALUES (82081,82081,1,'592 Tuscan appartment whitemall','Kaiser cross road','Bellevue','Washington','377719','USA','-14.833333333333334','38.2',NULL,NULL,1,'2014-01-21 00:00:00',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'ac7a0d4c-f954-11e3-8303-f0def1eaaa2d');
    
    elif(tableName=='person_address'):
        personAddress= person.address
        qStr+=str(idStart)+","
        qStr+=str(idStart)+","
        qStr+="1,"
        qStr+="'"+str(personAddress.houseNum) +" "+personAddress.address1+"',"
        qStr+="'"+personAddress.address2+"',"
        qStr+="'"+personAddress.city+"',"
        qStr+="'"+personAddress.state+"',"
        qStr+="'"+str(personAddress.postalCode)+"',"
        qStr+="'"+personAddress.country+"',"
        qStr+="'"+str(person.latitude)+"',"
        qStr+="'"+str(person.longitude)+"',"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="1,"
        qStr+="'2014-01-21 00:00:00',"
        qStr+="0,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="'"+person.uuid+"');"

#Format for patient_identifier   
#INSERT INTO `patient_identifier` VALUES (99,99,99,2,1,1,1,'2014-06-21 13:28:43', NULL, NULL,0, NULL, NULL, NULL,'8d79403a-c2cc-11de-8d13-0010c6dffd0f')
   
    elif(tableName=='patient_identifier'):
        qStr+=str(idStart)+","
        qStr+=str(idStart)+","
        qStr+=str(idStart)+","
        qStr+="2,"
        qStr+="1,"
        qStr+="1,"
        qStr+="1,"
        qStr+="'2014-01-21 00:00:00',"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="0,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="NULL,"
        qStr+="'"+person.uuid+"');"
    
    return qStr;