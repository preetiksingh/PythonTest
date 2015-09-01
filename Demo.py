import csv, sqlite3
conn = sqlite3.connect('db12')
conn.text_factory = str
curs = conn.cursor()

curs.execute("CREATE TABLE demo5(D1 text,D2 text,D3 integer,D4 text,D5 text,D6 text,D7 text,D8 text,D9 text);")
reader = csv.reader(open(r"data.csv", 'r'), delimiter=',')
for row in reader:
    to_db = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8])]
    curs.execute("INSERT INTO  demo5(d1, d2, d3, d4, d5, d6, d7, d8, d9) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()

for row in curs.execute("select * from demo4"):
    print row