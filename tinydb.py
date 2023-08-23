from tinydb import TinyDB  
from tinydb import Query
db=TinyDB('db.json')
user=Query()
def insert():
  db.insert({'name':'ram','age':22})
  db.insert({'name':'sam','age':26})
insert()
def search():
  result= db.search(user.name=='ram')
  

  print(result)


#print(db.all())