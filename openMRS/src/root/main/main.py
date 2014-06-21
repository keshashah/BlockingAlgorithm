

from root.utility import helper
from root.dataloader.patientLoader import insertScript
import codecs

# main program starts here...
dataFile = "C:\\Laptop\\GSOC\\openmrs\\generated_data\\blockingDemoData.csv"
numPatients = 100000
numPatientsWithDeath=25000
numDirtyPatients=10000

helper.writeToFileHeader(dataFile, "uuid,gender,age,birthDate,dead,deathDate,causeOfDeath,latitude,longitude,givenName,middleName,familyName,address1,address2,country")

patients = helper.getRandomPatientsData(numPatients, numPatientsWithDeath, numDirtyPatients)
#patients = helper.getRandomPatientsData(3, 1, 1)
helper.writeToFilePatients(dataFile, patients)

i = 0 
idStart = 1000
r = ""
f = codecs.open("C:\\Laptop\\GSOC\\openmrs\\generated_data\\insertScript.sql", 'w', "utf-8")

while (i<1):
    r += insertScript('person',patients[i],i+idStart)
    r += "\n"
    r += insertScript('person_name',patients[i],i+idStart)
    r += "\n"
    r += insertScript('person_address',patients[i],i+idStart)
    r += "\n"
    r += insertScript('patient_identifier',patients[i],i+idStart)
    r += "\n"
    f.write(r)
    r = ""
    i+=1
f.close()

print("Script generated successfully.")
