from revolut_handler import RevolutHandler

def main():

    handler = RevolutHandler("finante.db")

    handler.salveaza_csv_in_db("revolut.csv")

    tranzactii = handler.citeste_toate_tranzactiile()
    print(f"There are a total of {len(transactions)} transactions")
    print("Prima tranzacție stocată este:", transactions[0])

if __name__ == "__main__":
    main()