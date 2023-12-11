##Author: Ilyass Hmamoou
##Created: September 25, 2023
##Description: AnimalShelter class test file
###############################################################
###############################################################

from animalShelter import AnimalShelter
#instanciate AnimalShelter object
test = AnimalShelter('accuser','SNHU1234')
#define insert data
insertData =  {"1": 1,
               "age_upon_outcome": "3 year",
               "animal_id": "C123456",
               "animal_type": "Cat",
               "breed": "Domestic shorthair Mix",
               "color": "Brown",
               "date_of_birth": "2022-06-01",
               "datetime": "2023-01-01 10:00:00",
               "monthyear": "2023-01-01T10:00:00",
               "name": "Milo",
               "outcome_subtype": "SCRP",
               "sex_upon_outcome": "Fixed Male",
               "location_lat": 30.5635984560228,
               "location_long": -97.7419963476444,
               "age_upon_outcome_in_weeks": 30.506785
    
}
#test insert
createResponse = test.create(insertData)
print("Create response: ", createResponse)
#define read data
readData = {"animal_id": "C123456"}
#test read
readResponse = test.readAll({})
print("Read response: ", readResponse)
for doc in readResponse:
    print(doc)
#define update data
updateData = {"name":"Oreo"}
#test update
updateResponse = test.update(readData, updateData)
# read latest updated records to confirm name update from "Milo" to "Oreo"
readUpdated = test.read(readData)
print("Read Updated records: ")
for doc in readUpdated:
    print(doc)
#test delete
deleteResponse = test.delete(readData)
print("Total Deleted:", deleteResponse)
# read the record to confirm that it's not found
readDeleted = test.read(readData)
print("Read Deleted records: ")
for doc in readDeleted:
    print(doc)
