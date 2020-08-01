import sqlite3
import numpy as np

debug = True
def echo(*args,**kwargs):
    global debug
    if debug:
        print(*args,**kwargs)
    return

conn = sqlite3.connect('toymodel.db')
c = conn.cursor()
echo('DATABASE OPENED.')
events = []
px = []
py = []
c.execute('SELECT * FROM DES;')
num_events, max_mul = c.fetchone()
echo('THIS DATABASE HAS %d EVENTS, MAX MULTIPLICITY: %d.'%(num_events,max_mul))
for idx in range(1,num_events+1):
    c.execute('SELECT PX, PY FROM EV_%d;'%idx)
    px = []
    py = []
    data = None
    for item in c:
        px.append(item[0])
        py.append(item[1])
    data = np.array([px,py]).transpose()
    events.append(data)
    if idx%20 == 0:
        echo('EVENT %d LOADED.'%idx)
echo('DONE! %d EVENTS LOADED, MAX MULTIPLICITY: %d.'%(num_events,max_mul))
for idx in range(num_events):
    np.savetxt('./toymodel_data/%d.csv'%idx,events[idx],fmt='%.4f',delimiter=',')
    if idx%20 == 0:
        echo('EVENT %d SAVED.'%idx)
conn.close()

