#Divu tabulu savienošana

import sqlite3

db = sqlite3.connect('test.db')

dati = db.execute("""SELECT * FROM edienkarte
                  JOIN sastavdalas
                  ON edienkarte.id = sastavdalas.id
                  """)

rezultats = dati.fetchall()

print(rezultats)