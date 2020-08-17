import csv

#These functions mainly deals with vendor : category database functionalities.

#Fetches from existing/previously created database file with vendor : financial category mappings.
#categoryDBOath - String path to database file
def FetchCategoryDB(categoryDBPath):

    categoryDb = dict()

    with open(categoryDBPath, "r") as categoryDBFile:
        categoryDBReader = csv.DictReader(categoryDBFile)

        #Vendor
        #Category
        for categoryRow in categoryDBReader:
            categoryDb[categoryRow["Vendor"]] = categoryRow["Category"]

    return categoryDb

#Updates in-memory financial category mappings with vendor set.
#Vendors not in categoryDB will be added.
#vendorSet - Set of vendors - most likley retrieved from the current sent of new transactions.
#cateogyrDb - Dictionary database of vendor to category mappings, most likely constructed from file.
def UpdateWithVendors(vendorSet, categoryDB):
    addedVendors = 0

    for vendor in vendorSet:
        if vendor not in categoryDB:
            print("{} not in db".format(vendor))
            categoryDB[vendor] = ""
            addedVendors += 1

    print("Added {} vendor(s)".format(str(addedVendors)))

#Saves in memory category mappings into persistent file for use.
def SaveDb(categoryDBPath, categoryDB):
    print("Writing database to file {}".format(categoryDBPath))
    with open(categoryDBPath, "w", newline='') as csvFile:
        writer = csv.DictWriter(csvFile, ["Vendor", "Category"])
        writer.writeheader()

        for v, c in categoryDB.items():
            rowData = {"Vendor":v, "Category":c}
            writer.writerow(rowData)


#Debugging helpers
def PrintCategory(categoryDb):
    for vendor, category in categoryDb.items():
        print("{}={}".format(vendor, category))

    print("{} row(s)".format(len(categoryDb)))



#main

