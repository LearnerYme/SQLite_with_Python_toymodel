import sqlite3
import numpy.random as rd

debug = True
def echo(*args,**kwargs):
    global debug
    if debug:
        print(*args,**kwargs)
    return
#create a new .db file
conn = sqlite3.connect('toymodel.db')
c = conn.cursor()
echo('DATABASE OPENED.')
#create information table
c.execute('CREATE TABLE DES (NUM_EVENTS INT PRIMARY KEY, MAX_MUL INT);')
c.execute('INSERT INTO DES VALUES(0,0);')
echo('INFORMATION TABLE CREATED.')
#create dataset 
e_lambda = 300
p_lambda = 200
pid_list = [2212,-2212,321,-321,211,-211]
event_num = int(rd.poisson(e_lambda))
e_count = 0
max_mul = 0
for idx in range(1,event_num+1):
    c.execute('''CREATE TABLE EV_%d (ID INT PRIMARY KEY, PX REAL NOT NULL, PY REAL NOT NULL, 
                PID INT CHECK(PID IN (2212, -2212, 321, -321, 211, -211)));'''%idx)
    mul = rd.poisson(p_lambda)
    for particle in range(mul):
        px = rd.normal()
        py = rd.normal()
        pid = pid_list[rd.randint(6)]
        c.execute('INSERT INTO EV_%d VALUES(?,?,?,?);'%idx,(particle,px,py,pid))
    if max_mul < mul:
        max_mul = mul
        c.execute('UPDATE DES SET MAX_MUL = (?);',(max_mul,))
    e_count += 1
    c.execute('UPDATE DES SET NUM_EVENTS = (?);',(e_count,))
    if idx%20 == 0:
        echo('EVENT %d GENERATED.'%idx)
    conn.commit()
echo('DONE! NOW CLOSING FILE. TOTAL EVENTS: %d, MAX MULTIPLICITY: %d'%(e_count,max_mul))
conn.close()