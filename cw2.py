import sqlite3
connection = sqlite3.connect("istep_DB.sl3", 5)
cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
cur.execute("DELETE FROM first_table WHERE rowid=4;")
connection.commit()
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=4;")
# cur.execute("UPDATE first_table SET name='Sam' WHERE rowid=1;")
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()