import csv

class CitiTxProcessor:

    # Fetches only the vendors from Citi csv file, and returns all vendors
    # as a set.  In the csv, the vendors reside in the "Description" field
    def get_vendors_from_tx(self, citi_csv_path):
        vendor_set = set()

        with open(citi_csv_path, "r") as citi_csv_file:
            csv_reader = csv.DictReader(citi_csv_file)

            for csv_row in csv_reader:
                vendor_set.add(csv_row["Description"])

        return vendor_set

    # Reads into memory existing database on vendor & it's categories as a dictionary
    # The dictionary will be used later to cateogrized transactions.
    def load_categories_from_database(self, database_path):
        category_db = dict()

        with open(database_path, "r") as database_file:
            category_db_reader = csv.DictReader(database_file)

            # We are interested in the vendor and category mapping from the database file
            # and will read it into memory as a dictionary.
            for category_row in category_db_reader:
                category_db[category_row["Vendor"]] = category_row["Category"]

        return category_db


    def update_category_db_with_vendor_set(self, category_db, new_vendor_set):
        new_vendors_added = 0

        for vendor in new_vendor_set:
            if vendor not in category_db:
                print("{} not in db".format(vendor))

                category_db[vendor] = "TBD"
                new_vendors_added += 1

        print("Added {} vendor(s).".format(str(new_vendors_added)))

        return new_vendors_added

    def save_category_db(self, category_db, category_db_path):
        category_saved = 0
        print("Saving category database to file {}...".format(category_db_path))

        with open(category_db_path, "w", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, ["Vendor", "Category"])
            writer.writeheader()

            for v, c, in category_db.items():
                row_data = {"Vendor":v, "Category":c}
                writer.writerow(row_data)
                category_saved += 1

        print("Saved {} categories.".format(category_saved))



# Tests
def test_get_vendors_from_tx():
    citi_processor = CitiTxProcessor()
    print(citi_processor.get_vendors_from_tx("..\\Data2020\\Year to date.csv"))

def test_get_categories_from_database():
    citi_processor = CitiTxProcessor()
    print(citi_processor.load_categories_from_database("..\\Data2020\\categoryDb.csv"))

def test_save_category_db():
    citi_processor = CitiTxProcessor()

    vendors = citi_processor.get_vendors_from_tx("..\\Data2020\\Year to date.csv")
    category_db = citi_processor.load_categories_from_database("..\\Data2020\\categoryDb.csv")

    citi_processor.update_category_db_with_vendor_set(category_db, vendors)
    citi_processor.save_category_db(category_db, "..\\Data2020\\testdb.csv")



if __name__ == "__main__":
    print("Testing save category function.")
    input("Press any key to continue...")


    test_save_category_db()

    print("Done.")

else:
    print(__name__)

