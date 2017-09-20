import csv
from pymongo import MongoClient



#connecting to mongodb database
connection = MongoClient('localhost',27017)
db = connection.patients


patient_id = input("Enter patient id here: ")

#finding and accessing collections
results = db.patients.find()
results2= db.entrez.find()


#Querying given patient_id , find any information about the patient
for record in results:
    if (record['patient_id'] == patient_id):
        print("Age: {}, Gender: {}, Education: {}".format(record['age'], record['gender'], record['education']))
        break


for record2 in results2:
    if(record2['PATIENT_ID'] == patient_id):
        print("Diagnosis: {}".format(record2["DIAGNOSIS"]))
        break

#Querying given gene_id, compute Standard Deviation and Mean for certain diagnosis label
geneid = input("Please enter gene id here: ")

for getdiag in results2:
    diag = getdiag['DIAGNOSIS']
    gene_id = getdiag[geneid]
    patient_record = {'Diagnosis': diag, 'geneid': gene_id}
    db.record.insert(patient_record)

#aggregate function to retrieve standard deviation
stddev = db.record.aggregate([{"$group": {"_id": "$Diagnosis", "stdDev": {"$stdDevPop": "$geneid"  }}}, {"$sort":{"_id":1}}])

for all in stddev:
    print("Diagnosis label: {} ,Standard deviation: {} ".format(all['_id'], all['stdDev']))
#aggregate function to retrieve mean
avg = db.record.aggregate([{"$group": {"_id":"$Diagnosis", "Mean": {"$avg": "$geneid"}}}, {"$sort":{"_id":1}}])

print("--------------------------------------------------------------------------------")
for all in avg:
    print("Diagnosis label: {} , Mean: {}".format(all['_id'], all['Mean']))

#deleting record, just in case, database gets overloaded with data.
db.record.delete_many({})










