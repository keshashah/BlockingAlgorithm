
from root.blocking.blockingImpl import Blocking

blk = Blocking()
blockingPatients = blk.getNames()

for p in blockingPatients:
    sortedNameList = p.name.getSortedNamesAsList()
    p.setSortedNameList(sortedNameList)
    
blkCol1 = blk.blockingScheme1(blockingPatients)

#blkCol2 = blk.blockingScheme2(blockingPatients)

    
