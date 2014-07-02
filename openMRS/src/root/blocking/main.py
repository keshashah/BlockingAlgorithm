
from root.blocking.blockingImpl import Blocking

blk = Blocking()
blockingPatients = blk.getNames()

#SortedNamesList-Separate-NoPhoneticTransform
for p in blockingPatients:
    sortedNameList = p.name.getSortedNamesAsList()
    p.setSortedNameList(sortedNameList)
    
blkCol1 = blk.SortedBlockingScheme1(blockingPatients)

blkCol2 = blk.SortedBlockingScheme2(blockingPatients)

blkCol3 = blk.SortedBlockingScheme3(blockingPatients)
    
blkCol4 = blk.SortedBlockingScheme4(blockingPatients)

blkCol5 = blk.SortedBlockingScheme5(blockingPatients)

#Truncate blockingscheme table first
blk.truncateBlockingSchemeTable()
#update the blockingscheme table in the database
blk.insertBlockingSchemeTable("scheme1","sorted-separate-noPhoneticTransform",blkCol1)
blk.updateBlockingSchemeTable("scheme2","sorted-separate-noPhoneticTransform",blkCol2)
blk.updateBlockingSchemeTable("scheme3","sorted-separate-noPhoneticTransform",blkCol1)
blk.updateBlockingSchemeTable("scheme4","sorted-separate-noPhoneticTransform",blkCol1)
blk.updateBlockingSchemeTable("scheme5","sorted-separate-noPhoneticTransform",blkCol1)


#UnSortedNamesList-Separate-NoPhoneticTransform
for p in blockingPatients:
    UnSortedNameList = p.name.getUnSortedNamesAsList()
    p.setUnSortedNameList(UnSortedNameList)

blkCol1 = blk.UnSortedBlockingScheme1(blockingPatients)

blkCol2 = blk.UnSortedBlockingScheme2(blockingPatients)

blkCol3 = blk.UnSortedBlockingScheme3(blockingPatients)
    
blkCol4 = blk.UnSortedBlockingScheme4(blockingPatients)

blkCol5 = blk.UnSortedBlockingScheme5(blockingPatients)

#Truncate blockingscheme table first
blk.truncateBlockingSchemeTable()
#update the blockingscheme table in the database
blk.insertBlockingSchemeTable("scheme1","unsorted-separate-noPhoneticTransform",blkCol1)
blk.updateBlockingSchemeTable("scheme2","unsorted-separate-noPhoneticTransform",blkCol2)
blk.updateBlockingSchemeTable("scheme3","unsorted-separate-noPhoneticTransform",blkCol1)
blk.updateBlockingSchemeTable("scheme4","unsorted-separate-noPhoneticTransform",blkCol1)
blk.updateBlockingSchemeTable("scheme5","unsorted-separate-noPhoneticTransform",blkCol1)


