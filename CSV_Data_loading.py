import os
import csv
import mysql.connector

csv_path = input("Enter full path to your CSV file: ").strip()

if not os.path.isfile(csv_path):
    print(" File does not exist. Please check the path and try again.")
    exit()

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='HelloChintu@1996',
        database='ashok_sql_class'
    )
    cursor = conn.cursor()
    print(" Connected to MySQL database.")
except mysql.connector.Error as err:
    print(" Connection error:", err)
    exit()

insert_query = """
    INSERT INTO student_profile (
        College_ID, IQ, Prev_Sem_Result, CGPA, Academic_Performance,
        Internship_Experience, Extra_Curricular_Score,
        Communication_Skills, Projects_Completed, Placement
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    with open(csv_path, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        data_to_insert = [tuple(row) for row in reader]

        cursor.executemany(insert_query, data_to_insert)
        conn.commit()
        print(f"{cursor.rowcount} records inserted successfully.")

except Exception as e:
    print("Error during CSV insert:", e)
finally:
    cursor.close()
    conn.close()
    print("Connection closed.")
