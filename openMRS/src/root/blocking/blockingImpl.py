
from root.models.name import Name
from root.models.blockingPatient import BlockingPatient

class Blocking:
    
    def getNames(self):
        import pymysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')  # else connect to default mysqldb
        cur = conn.cursor()
        query = 'select pn.uuid,pn.given_name,pn.middle_name,pn.family_name,SUBSTR(YEAR(pe.birthdate),-2) from person pe,person_name pn where pe.uuid=pn.uuid limit 1'
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

blk = Blocking()
patients = blk.getNames()


