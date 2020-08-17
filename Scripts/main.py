import GetTxVendors as tx
import CategoryDB as db

#GetTxVendors
txVendors = tx.GetTxVendors("", "..\Data\Year To Date.csv")
#tx.PrintTxVendors(txVendors)

#FetchCategoryDB
categoryDb = db.FetchCategoryDB("..\Data\categoryDB.csv")

#db.PrintCategory(categoryDb)

db.UpdateWithVendors(txVendors, categoryDb)

db.SaveDb("..\Data\categoryDB.csv", categoryDb)
