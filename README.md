# SQLite_with_Python_toymodel
This is a demo that uses python to operate sqlite database using a toy model of simulating the information on the final state particles of high-energy nuclear collisions. Actually, the so-called toymodel is just using a Gaussian distribution.^^

The main idea of this repository is that to show how to create, read and edit SQLite database via python. Basic knowledge of SQLite and Python is needed.

**Usage**

Firstly, run ``python generate_db.py``, and a database 'toymodel.db' will be created in a few seconds. You can then run ``sqlite3 toymodel.db`` to see details about this database.

Then, run ``python load_db.py``, and seires of '.csv' files will be created under the directory './toymodel_data/'.
