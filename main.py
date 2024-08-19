import pandas as pd
import csv
import datetime as datetime

class CSV:
    CSV_FILE = "finance.csv"
    
    @classmethod
    def initialise_csv(self):
        try:
            pd.read_csv(self.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date","amount","category","description"])
            df.to_csv(self.CSV_FILE, index=False)
            
CSV.initialise_csv()            