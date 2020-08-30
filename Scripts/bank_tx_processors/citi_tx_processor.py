class CitiTxProcessor:
    def get_vendors_from_tx(self, tx_path):
        return "get_vendors_from_tx:" + tx_path

    def get_categories_from_file(self, category_path):
        return "get_categoreis_from_db:" + category_path

    def update_category_db_with_new_vendors(self, vendors):
        return "update_category_db_with_new_vendors:" + vendors

    def save_category_to_file(self, category_path):
        return "save_category_to_file:" + category_path

#missing an __init__??

def main():
    citi_processor = CitiTxProcessor()

    print(citi_processor.get_vendors_from_tx("foo"))
    print(citi_processor.get_categories_from_file("foo"))
    print(citi_processor.update_category_db_with_new_vendors("foo"))
    print(citi_processor.save_category_to_file("foo"))


if __name__ == "__main__":
    main()
else:
    print(__name__)


