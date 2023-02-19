import sqlite3
from sqlite3 import Error 
import sys
import os
import glob

## Get paths and combine to create full path
absolute_path = os.path.dirname(__file__)
relative_path = "databases/"

print("*** The following database files are available: ***")
database_files_path = glob.glob(relative_path + '*', recursive=False)
for filename in database_files_path:
    print(filename)
print("\n") ## Blank line

# #res_str_relative_path = database_files_path.translate({ord('/'): None})
# print(res_str_relative_path)

## def file_check_function():
#    print(os.system("ls -la" + res_str_relative_path))

# file_check_function()

db_file = input("What database do you want to connect to? ") # Accept user input to define file name
full_path = os.path.join(absolute_path, relative_path, db_file)
print("\n") ## Blank line


def create_sql_connection(db_file):
    """ create a connection to local database """
    conn = None
    try: 
        conn = sqlite3.connect(db_file)
        print("Connected to SQLite Database..")
        print("The current version of this database is: " + sqlite3.version)

        
    except Error as e:
        print(e)
    finally: 
        if conn:
            conn.close()

if __name__ == '__main__':
    create_sql_connection(full_path) 