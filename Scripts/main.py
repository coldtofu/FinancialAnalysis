import GetTxVendors as tx
import CategoryDB as db

#GetTxVendors
txVendors = tx.GetTxVendors("", "..\Data\Year To Date.csv")
print("Found {} vendor(s) in this csv".format(len(txVendors)))
input("Press any key to continue...")
#tx.PrintTxVendors(txVendors)

#FetchCategoryDB
categoryDb = db.FetchCategoryDB("..\Data\categoryDB.csv")
print("Foud {} categories in DB.".format(len(categoryDb)))
input("Press any key to continue...")

#db.PrintCategory(categoryDb)


db.UpdateWithVendors(txVendors, categoryDb)

#db.SaveDb("..\Data\categoryDB.csv", categoryDb)
