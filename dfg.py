L=[[1,'Ajay'],[2,'Sanjay']]
from cx_Oracle import *
con=connect('system','123456')
cur=con.cursor()
cur.executemany("insert into hp values(:1,:2)",(L))
con.commit()
