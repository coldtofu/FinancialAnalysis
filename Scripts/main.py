import GetTxVendors as tx
import CategoryDB as db

#GetTxVendors
#todo: First argument should be removed, redundant.
txVendors = tx.GetTxVendors("", "..\Data\Year To Date.csv")
print("Found {} vendor(s) in this csv".format(len(txVendors)))
input("Press any key to continue...")
#tx.PrintTxVendors(txVendors)

#FetchCategoryDB
categoryDb = db.FetchCategoryDB("..\Data\categoryDB.csv")
print("Found {} categories in DB.".format(len(categoryDb)))
input("Press any key to continue...")

#db.PrintCategory(categoryDb)


#db.UpdateWithVendors(txVendors, categoryDb)
#db.SaveDb("..\Data\categoryDB.csv", catego
# ryDb)

#Date:Description:Debit:Credit:Category
txList = tx.GetTxAsList("..\Data\Year To Date.csv")
print(txList)

categoryDb = db.FetchCategoryDB("..\Data\categoryDB2.csv")
print(categoryDb)
