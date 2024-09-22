from testdata import generate_test
import json
import csv
import os
# Open and read the JSON file
def process(filename):
    with open('/Users/binufamily/MyProjects/v2AmmavanCode/filecatcher/'+filename, 'r') as file:
        data = json.load(file)
    # Print the data
    print(type(data))
    print(data['regex'])
    fields = list(data['regex'].keys())
    print(fields)
    # name of csv file
    filename = "records.csv"
    # writing to csv file
    pdata=[]
    for j in range(data['tests']):
        mydict = {}
        for i in range(len(fields)):
            mydict[fields[i]] = (generate_test(data['regex'].get(fields[i])))
        print(mydict)
        pdata.append(mydict)
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # writing headers (field names)
        writer.writeheader()
        # writing data rows
        writer.writerows(pdata)
        return os.path.abspath(filename)
        