
import pymysql
conn=pymysql.connect(

    host='localhost',
    user='root',
    password='root',
    db='crimedb',
)

print('Checking the connection')
print(conn)
cur=conn.cursor()
str1='Select * from crimedb.crime_data limit 2'
cur.execute(str1)
res=cur.fetchall()
for i in res:
    print(i)