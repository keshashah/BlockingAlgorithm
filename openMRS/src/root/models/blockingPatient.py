class BlockingPatient :
    '''
    BlockingPatient Class - contains fieds required for processing blocking algorithms/schemes
    '''
                
    def setName(self,name):
        self.name = name   

    def setUuid(self,uuid):
        self.uuid = uuid
        
    def setYob(self,yob):
        self.yob = yob     
    
    def setMob(self,mob):
        self.mob = mob     
    
    def setDayob(self,dayob):
        self.dayob = dayob     
    
    def setSortedNameList(self,snl):
        self.sortedNameList = snl
    
    def setUnSortedNameList(self,unl):
        self.UnSortedNameList = unl
    
    def __str__(self):
            return(self.uuid + ","+str(self.name)+","+str(self.yob))