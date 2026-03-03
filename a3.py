import pandas as pd
import sqlite3

database='basketball.sqlite'

conn=sqlite3.connect(database)

tables=pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE type='table';""", conn)
print(tables)

empty1=pd.read_sql("""SELECT *
                    FROM Draft
                   WHERE locationOrganizationFrom IS NULL;""", conn)
print(empty1)

earliest5teams=pd.read_sql("""SELECT *
                            FROM Team
                            ORDER BY year_founded
                            LIMIT 5;""", conn)

print(earliest5teams)

latest5teams=pd.read_sql("""SELECT *
                            FROM Team
                            ORDER BY year_founded DESC
                            LIMIT 5;""", conn)

print(latest5teams)