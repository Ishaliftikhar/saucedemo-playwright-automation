import csv

def save_products_to_csv(products, file_path):
    with open(
        file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Description", "Price"])

        writer.writeheader()
        writer.writerows(products)