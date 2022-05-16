import sqlite3
import csv

def extract_db(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    with open(f"monlam.csv","w") as f:
        writer = csv.writer(f)
        for row in cur.execute('SELECT word text,definition text FROM tbtb'):
            word,desc = row     
            writer.writerow([word,desc])
    con.close()


if __name__ == "__main__":
    name = "MLDic.sqlite"
    extract_db(name)