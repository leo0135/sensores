import mysql.connector
import random
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="leo.0135",
    database="aquaflow_db"
)
cursor = conn.cursor()

for i in range(20):
    ph = round(random.uniform(6.5, 8.5), 2)
    turbidez = round(random.uniform(1, 10), 2)
    cursor.execute(
        "INSERT INTO sensores (ph, turbidez) VALUES (%s, %s)",
        (ph, turbidez)
    )
    conn.commit()
    print(f"Registro {i+1}: pH={ph}, Turbidez={turbidez}")
    time.sleep(2)

cursor.close()
conn.close()
