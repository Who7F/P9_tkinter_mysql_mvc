
import sqlite3


class SQLhelp:
    def __init__(self, name):
        self.db='data/test.db'
        self.table = name
        
        
    def dropE(self):
        return ("DROP TABLE IF EXISTS " + self.table)
    def create_table(self):
        return ("CREATE TABLE " + self.table + " (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, colour TEXT NOT NULL, make TEXT NOT NULL)")
    def insert(self):
        return("INSERT INTO " + self.table + " (name, colour, make) VALUES (?, ?, ?)")
    def test(self):
        print(self.db)
        
        
def SQLping():
    print('ping')
    
class stockSQL:
    def insertDemo (item):
        return ("INSERT INTO example_table (field1, field2, field3) VALUES (?, ?, ?)", (item["field1"], item["field2"], item["field3"]))
    def something():
        return cur.executemany("INSERT INTO " + f.table_1 + " VALUES(?,?,?,?)", temp_data)
    
def main():
    print('SQLcontrolls')

if __name__ == "__main__":
    main()
