from pymongo import Connection

conn = Connection()
db = conn.test1 
db.drop_collection('todo')



