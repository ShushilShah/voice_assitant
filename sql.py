import sqlite3

connection = sqlite3.connect("content.db")

cursor = connection.cursor()

# creating table

table_info = """
Create table CONTENT(QUERY VARCHAR(255), RESPONSE VARCHAR(255));

"""

cursor.execute(table_info)

# Insert data
cursor.execute('''Insert into CONTENT values('name','My name is Talker')''')
cursor.execute('''Insert into CONTENT values('capital','kathmandu')''')


# Displaying data

print("The inserted data")
data = cursor.execute('''SELECT * from CONTENT''')

for row in data:
    print(row)

connection.commit()
connection.close()
