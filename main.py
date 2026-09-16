from importFromCsv import import_transactions


def main():
    file="revolut.csv"
    all_transactions=import_transactions(file)
    print("The first transaction is ")
    print(all_transactions[0])
if __name__=="__main__":
    main()