import sqlite3
import sys
import os

## Get paths and combine to create full path
absolute_path = os.path.dirname(__file__)
relative_path = "databases/"

database_files_list = os.listdir(relative_path) # Creat db file list using defined relative path
for file_names in database_files_list # Loop and print db files from relative path

db_file = input("What database do you want to connect to? ") # Accept user input to define file name
full_path = os.path.join(absolute_path, relative_path, db_file)
os.getcwd()

print(absolute_path + "; This is the absolute path")
print(relative_path + "; This is relative path")
print(full_path + "; This is the full path")


def create_sql_connection(db_file):
    """ create a connection to local database """
    conn = None
    try: 
        conn = sqlite.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally: 
        if conn:
            conn.close()

if __name__ == '__main__':
    create_sql_connection(full_path)

