
from root.models.name import Name
from root.models.blockingPatient import BlockingPatient

class Blocking:
    
    def getNames(self):
        import pymysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')  # else connect to default mysqldb
        cur = conn.cursor()
        query = "select pn.uuid,pn.given_name,pn.middle_name,pn.family_name,DATE_FORMAT(pe.birthdate,'%y'),DATE_FORMAT(pe.birthdate,'%m'),DATE_FORMAT(pe.birthdate,'%d') from person pe,person_name pn where pe.uuid=pn.uuid"
        query += " limit 100"
        cur.execute(query)
        blockingPatients = []
                
        for row in cur:
            uuid = row[0]
            givenName = row[1]
            middleName = row[2]
            familyName = row[3]
            yob = row[4]
            mob = row[5]
            dayob = row[6]
            name = Name(givenName, middleName, familyName)
            p = BlockingPatient()
            p.setName(name)
            p.setUuid(uuid)
            p.setYob(yob)
            p.setMob(mob)
            p.setDayob(dayob)
            blockingPatients.append(p)
            
        cur.close()
        conn.close()
        return blockingPatients
    
    
    #[ B3, C3, Y2 ] First 3 characters of Names B and Name C and the last 2 digits of the year of birth (JUDWAW80)
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
    
    #[ B3, Blk-DB , Blk-MB ] First 3 characters of Name B, date and month of birth (JUD2703)
    def blockingScheme2(self,blockingPatients):
        blockingColumn = {}
        for p in blockingPatients:
            b = p.sortedNameList[1]
            b = b[0:3]
            s = b + p.dayob + p.mob
            blockingColumn.update({str(p.uuid) : s.upper()})
        return blockingColumn
                
    #[ C3, Blk-DB, Blk-MB ] First 3 characters of Name C, date and month of birth (WAW2703)
    def blockingScheme3(self,blockingPatients):
        blockingColumn = {}
        for p in blockingPatients:
            c = p.sortedNameList[2]
            c = c[0:3]
            s = c + p.dayob + p.mob
            blockingColumn.update({str(p.uuid) : s.upper()})
        return blockingColumn
        
    #[ B1, YB, Blk-DB, Blk-MB ] First character of Name B and date of birth (J032780)
    def blockingScheme4(self,blockingPatients):
        blockingColumn = {}
        for p in blockingPatients:
            b = p.sortedNameList[1]
            b = b[0:1]
            s = b + p.mob + p.dayob + p.yob
            blockingColumn.update({str(p.uuid) : s.upper()})
        return blockingColumn
    
    #[ C1, YB, Blk-DB, Blk-MB ] First character of Name C and date of birth (W032780)
    def blockingScheme5(self,blockingPatients):
        blockingColumn = {}
        for p in blockingPatients:
            c = p.sortedNameList[2]
            c = c[0:1]
            s = c + p.mob + p.dayob + p.yob
            blockingColumn.update({str(p.uuid) : s.upper()})
        return blockingColumn
    
    
    def insertBlockingSchemeTable(self,schemeName,blockingColumn):
        import pymysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')  # else connect to default mysqldb
        cur = conn.cursor()
        
        for value in blockingColumn:
            query = "REPLACE INTO blockingscheme (uuid,"+schemeName+") values('"+value+"','"+blockingColumn[value]+"')"
            cur.execute(query)
        
        conn.commit()    
        cur.close()
        conn.close()
        return
    
    
    def updateBlockingSchemeTable(self,schemeName,blockingColumn):
        import pymysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='openmrs')  # else connect to default mysqldb
        cur = conn.cursor()
        
        for value in blockingColumn:
            query = "UPDATE blockingscheme set "+schemeName+" = '"+blockingColumn[value]+"' where uuid='"+value+"'"
            cur.execute(query)
        
        conn.commit()    
        cur.close()
        conn.close()
        return
            
    
    
    