
from root.models.name import Name
from root.models.blockingPatient import BlockingPatient

class Blocking:
    
    def getNames(self):
        import pymysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')  # else connect to default mysqldb
        cur = conn.cursor()
        query = 'select pn.uuid,pn.given_name,pn.middle_name,pn.family_name,SUBSTR(YEAR(pe.birthdate),-2) from person pe,person_name pn where pe.uuid=pn.uuid limit 10'
        cur.execute(query)
        blockingPatients = []
                
        for row in cur:
            uuid = row[0]
            givenName = row[1]
            middleName = row[2]
            familyName = row[3]
            yob = row[4]
            name = Name(givenName, middleName, familyName)
            p = BlockingPatient()
            p.setName(name)
            p.setUuid(uuid)
            p.setYob(yob)
            blockingPatients.append(p)
            
        cur.close()
        conn.close()
        return blockingPatients
    
    
    #[ B3, C3, Y2 ] First 3 characters of Names B and Name C and the last 2 digits of the year of birth (JUDWAW80a)
    def blockingScheme1(self,blockingPatients):
        blockingColumn = {}
        for p in blockingPatients:
            b = p.sortedNameList[1]
            c = p.sortedNameList[2]
            b = b[0:3]
            c = c[0:3]
            s = b + c + p.yob
            blockingColumn.update({str(p.uuid) : s.upper()})
        return blockingColumn
        
        