import tkinter
from PIL import ImageTk
import sqlite3
import json
import csv
from controller import stockSQL as sS
from view import view as mV

temp_data = [
    (0, 'sup','git','hellp'),
    (1, 'sup','git','hellp'),
    (2, 'sup','git','hellp')
             ]

class P9verbals:
    bg='#3d6466'
                
def connect():
    f = sS.SQLhelp('cars')
    f.test()
    conn = sqlite3.connect(f.db)
    cur = conn.cursor()
    print(f.dropE())
    cur.execute(f.dropE())
    cur.execute(f.create_table())
    cur.executemany("INSERT INTO " + f.table + " VALUES(?,?,?,?)", temp_data)
    bugger = {'name':'rick', 'colour':'blue','make':'your mum'}
    cur.execute(f.insert(), ('rick', 'blue','your mum'))

    for i in cur.execute("SELECT * FROM " + f.table):
        print(i)
    conn.close

def importCSV(fill):
    with open(fill) as csvfile:
        spam_reader = csv.reader(csvfile, delimiter = ',')
        for i in spam_reader:
            print(i)
        
def load_frame1():
    print('bag of dicks')
    
    #importCSV('P5TestPlan.csv')
    
    
def load_frame2():
    test = Model('pop', 1995)
    sup = test.getAll()
    print(sup['date'])

def load_frame3():
    connect()
    print('butts')

def test():
    load_frame2()


def main():
    root = tkinter.Tk()
    root.title('Hello')
    #root.eval('tk::PlaceWindow . center')
    

    x = int(root.winfo_screenwidth() // 2)
    y = int(root.winfo_screenheight() * 0.1)
    print(x, y)

    root.geometry('500x600+' + str(x) + '+' + str(y))

    #tkinter.Frame(root, width=500, height=400, bg=P9verbals.bg).grid(row = 0, column = 0)
    frame_1 = tkinter.Frame(root, width=500, height=600, bg=P9verbals.bg)
    frame_2 = tkinter.Frame(root, bg=P9verbals.bg)
    frame_1.grid(row = 0, column = 0)
    for frame in (frame_1, frame_2):
        frame.grid(row = 0, column = 0)
    
    mV.load_main(frame_1, 'assets/rickroll.png')

    root.mainloop()


if __name__ == "__main__":
    main()
