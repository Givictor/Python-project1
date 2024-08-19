import pandas as pd
import csv
import datetime as datetime

class CSV:
    CSV_FILE = "finance.csv"
    COLUMNS = ["date","amount","category","description"]
    
    @classmethod
    def initialise_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date","amount","category","description"])
            df.to_csv(cls.CSV_FILE, index=False)
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry= {
            "date": date,
            "amount": amount,
            "category" : category,
            "description" : description
        }
        
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("New Entry added Successfully")
            
            
CSV.initialise_csv()
CSV.add_entry("19-08-2024",200,"Fees","SecondMonth")           