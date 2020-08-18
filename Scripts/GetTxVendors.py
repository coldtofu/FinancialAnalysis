import csv

#These function mainly deals with new monthly transctions - downloaded from banks, etc.

#Read in existing VendorDB to create in memory DB (as a set)
#Read in Citibank transactions as a LIST
#For each vendor transaction in LIST not in VendorDB, add to VendorDB.
#Write out VendorDB Dictionary to file.

#Extracts all vendor from transaction file provided by vendorDBPath
def GetTxVendors(citiTxFilePath, vendorDBPath):
    vendorDB = set()

    with open(vendorDBPath, "r") as vendorDBFile:
        csvVendorDBReader = csv.DictReader(vendorDBFile)

        #Date, Description, Debit, Credit, Category
        for csvVendorDBRow in csvVendorDBReader:
            vendorDB.add(csvVendorDBRow["Description"])
            #print("{}/{}/{}/{}/{}".format(csvVendorDBRow["Date"], csvVendorDBRow["Description"], csvVendorDBRow["Debit"], csvVendorDBRow["Credit"], csvVendorDBRow["Category"]))

    return vendorDB

def GetTxAsList(citiTxFilePath):
    transactions = []

    with open(citiTxFilePath, "r") as txFile:
        txReader = csv.DictReader(txFile)

        for txRow in txReader:
            transactions.append(txRow)

    return transactions

def PrintTxVendors(db):
    for r in db:
        print(r)
    print("{} row(s)".format(len(db)))

#vendorsFromTx is a set


#main

#txVendors = GetTxVendors("", "..\Data\Year To Date.csv")
#PrintTxVendors(txVendors)


