import pymysql

con = None
cur = None

def dbconnect():
    global con,cur
    try:
        con = pymysql.connect(host='localhost',
                        database='bank',
                        user='root',
                        password='')
        cur = con.cursor()
    except Exception as e:
        print(e)

def dbdisconnect():
    con.close()

def showcustomer():
 dbconnect()
 query='select * from customer'
 cur.execute(query)
 records=cur.fetchall()
 dbdisconnect()
 return records   



def Create( accno,name,city,contact,adhaarcard,pin,balance):
    dbconnect()
    query = f'insert into customer(accno,name,city,contact,adhaarcard,pin,balance) values ({accno},"{name}","{city}",{contact},{adhaarcard},{pin},{balance})'
   
    cur.execute(query)
    con.commit()
    dbdisconnect()

def Deposist(pin,amount,accno,type):
    dbconnect()
    query1=f'update customer set balance=balance+{amount} where pin={pin}'
    query2=f'insert into transaction(accno,amount,type) values({accno},{amount},"{type}")'
    cur.execute(query1)
    cur.execute(query2)
    con.commit()
    dbdisconnect()

def Withdrawn(pin,amount,accno,type):
    dbconnect()
    query1=f'update customer set balance=balance-{amount} where pin={pin}'
    query2=f'insert into transaction(accno,amount,type) values({accno},{amount},"{type}")'

    cur.execute(query1)
    cur.execute(query2)
    con.commit()
    dbdisconnect()


def updatename(pin,newname):
    dbconnect()
    query=f'update customer set name="{newname}" where pin={pin}'
    cur.execute(query)
    con.commit()
    dbdisconnect()

def showtransaction():
    dbconnect()
    query = 'select * from transaction'
    cur.execute(query)
    records = cur.fetchall()
    dbdisconnect()
    return records

def deleteaccount(pin):
    dbconnect()
    query = f"delete from customer where pin={pin}"
    cur.execute(query)
    con.commit()
    dbdisconnect()






