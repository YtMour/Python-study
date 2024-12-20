from tinydb import TinyDB, Query

db = TinyDB('tiny.db')
query = Query()

# db.insert({'name': 'John', 'age': 25})
# db.insert_multiple([
#     {'name': 'Jane', 'age': 30},
#     {'name': 'Bob', 'age': 35}
# ])


print(db.all())
for line in db:
    print(line)

print('=============')
result = db.search(query.name == 'Bob')
print(result)

# print('=============')
# db.update({'name':'tttt'},query.name =='Bob')
# print(db.all())


#选择性清除
# db.remove(query.name == 'tttt')
# print(db.all())

#全部清除
db.truncate()
print(db.all())
