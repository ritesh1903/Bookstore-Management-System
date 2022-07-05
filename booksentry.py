import sqlite3
db=sqlite3.connect("m5.db")
cur=db.cursor()
for x in range(5):
    
    ttl=input("enter book's title: ")
    aut=input("enter name of author: ")
    pr=float(input("enter price: "))
    sql="INSERT INTO books (title, author, price) VALUES ('"+ttl+"','"+aut+"','"+str(pr)+"');"

    try:
        cur=db.cursor()
        cur.execute(sql)
        db.commit()
        print ("one record added successfully")
    except:
        print ("error in operation")
        db.rollback()
db.commit()

