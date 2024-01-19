import sqlite3

connection = sqlite3.connect("content.db")

cursor = connection.cursor()

# creating table

table_info = """
Create table CONTENT(QUERY VARCHAR(255), RESPONSE VARCHAR(255));

"""

cursor.execute(table_info)

# Insert data
cursor.execute(
    '''Insert into CONTENT values('hello','Hello! how can I help you?')''')
# cursor.execute('''Insert into CONTENT values('name','My name is Talker')''')
cursor.execute('''Insert into CONTENT values('capital','kathmandu')''')
cursor.execute(
    '''Insert into CONTENT values('I love you','Sorry, I am a machine. I do not have any feelings')''')
cursor.execute(
    '''Insert into CONTENT values('I hate you','Sorry, I am a machine. I do not have any feelings')''')
cursor.execute(
    '''Insert into CONTENT values('Ram','Lord Rama is a hindu religion god known as Purusotam Ram')''')
cursor.execute(
    '''Insert into CONTENT values('who am i','You are Shushil Shah who built me.')''')


# Displaying data

print("The inserted data")
data = cursor.execute('''SELECT * from CONTENT''')

for row in data:
    print(row)

connection.commit()
connection.close()
