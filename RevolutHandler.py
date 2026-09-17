import csv
import sqlite3

class Revoluthandler:
    def __init__(self,db_name="finance.db"):
        self.db_name=db_name
        self.create_table()
    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor=conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT,
                    category TEXT,
                    sum REAL,
                    data TEXT
                )
            """)
    def save_csv_in_db(self,name_file_csv):
        transactions=[]
        with open(name_file_csv,mode="r",encoding="utf-8") as file:
            reader=csv.DictReader(file)
            for rand in reader:
                descripton = rand.get("Description", "No description")
                category = rand.get("Category") or "Uncategorized"
                try:
                    sum=float(rand.get("Amount",0.0))
                except(ValueError,TypeError):
                    sum=0.0
                data=rand.get("Started Date","")
                transactions.append((descripton,category,sum,data))


            