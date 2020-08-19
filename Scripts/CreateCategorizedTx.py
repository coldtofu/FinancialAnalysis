import GetTxVendors as tx
import CategoryDB as db
import csv

#Combines raw citi transactions, and my own categories per vendor
#into a categorized transaction list to be analyzed via a spreadsheet

#1. Get raw citi transaction
txList = tx.GetTxAsList("..\Data\Year To Date.csv")

#2. Get categorized vendor list
categorizedVendor = db.FetchCategoryDB("..\Data\categoryDB2.csv")

#3. Create a new dictionary, merged with proper category
mergedList = []

#Date, Description, Debit, Credit, Category
for tx in txList:
    vendor = tx["Description"]
    financialCategory = categorizedVendor[vendor]
    tx["FCategory"] = financialCategory

    #print("{} is categorized as {}".format(vendor, financialCategory))
    #input("press any key to continue to merge...")

with open("report.csv", "w", newline='') as csvFile:
    writer = csv.DictWriter(csvFile, ["Date", "Description", "Debit", "Credit", "Category", "FCategory"])
    writer.writeheader()

    for row in txList:
            writer.writerow(row)



