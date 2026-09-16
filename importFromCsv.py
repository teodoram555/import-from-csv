import csv

def categorize_transactions(description):
    revolut_category=description.get("Category")
    if not revolut_category:
        return "Uncategorized"
    return revolut_category

def import_transactions(name_file):
    transactions=[]
    with open(name_file,mode="r",encoding="utf-8") as file:
        reader=csv.DictReader(file)
        for rand in reader:
            rand["Category"]=categorize_transactions(rand)
            transactions.append(rand)
    return transactions

