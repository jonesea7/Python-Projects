import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_person(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_fname TEXT,\
                col_lname TEXT,\
                    col_email TEXT)")
    conn.commit()

conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_person(col_fname,col_lname,col_email) VALUES (?,?,?)",\
        ('Bob', 'Smith', 'bsmith@aol.com'))
    cur.execute("INSERT INTO tbl_person(col_fname,col_lname,col_email) VALUES (?,?,?)",\
        ('John', 'Lithgow', 'funnyman@aol.com'))
    cur.execute("INSERT INTO tbl_person(col_fname,col_lname,col_email) VALUES (?,?,?)",\
        ('Cookie', 'Monster', 'cookie@aol.com'))
    conn.commit()

conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_person WHERE col_fname = 'Cookie'")
    varPerson = cur.fetchall()
    for col in varPerson:
        message = f"First Name: {col[0]} \nLast Name: {col[1]} \nEmail: {col[2]}"
    print(message)