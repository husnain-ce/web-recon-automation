
import mysql.connector
from mysql.connector import Error

def setup_database(project_name):
    try:
        db = mysql.connector.connect(host="localhost", user="creadentials", password="yours_pass", database=project_name)
        cursor = db.cursor()

        # Create tables if not exists
        cursor.execute("CREATE TABLE IF NOT EXISTS domains (name VARCHAR(255), ip VARCHAR(255))")
        cursor.execute("CREATE TABLE IF NOT EXISTS nmapscan (ip VARCHAR(255), open_ports VARCHAR(255))")
        cursor.execute("CREATE TABLE IF NOT EXISTS gobuster (domain VARCHAR(255), result LONGTEXT)")

        return db, cursor

    except Error as e:
        print("Error while connecting to MySQL", e)

