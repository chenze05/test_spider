# csv 1
# import csv
# with open('data.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow([1, 'hanson', 28])
#     writer.writerow([2, 'xiaoma', 23])
#     writer.writerows([[3, 'luffy', 19], [4, 'robin', 27]])

# csv 2
# import csv
# with open('data2.csv', 'w', newline='') as csv_file:
#     field_names = ['id', 'name', 'age']
#     writer = csv.DictWriter(csv_file, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerow({'id': 1, 'name': 'hanson', 'age': 28})

# csv 3
# import csv
# with open('data.csv', 'r', encoding='utf-8') as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)
#         # print(type(row))




# mysql 1
# import pymysql
#
# user = 'root'
# password = 'chenze'
# host = 'localhost'
# port = 3306
#
# db = pymysql.connect(host=host, user=user, password=password, port=port)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('database version: {}'.format(data))
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET UTF8MB4')
# db.close()


# mysql2
# import pymysql
# username = 'root'
# password = 'chenze'
# host = 'localhost'
# port = 3306
# db_name = 'spiders'
#
# db = pymysql.connect(host=host, port=port, user=username, password=password, db=db_name)
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, ' \
#       'name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# mysql3
# import pymysql
# username = 'root'
# password = 'chenze'
# host = 'localhost'
# port = 3306
# db_name = 'spiders'
#
# id = '2009003'
# name = 'xiaoma'
# age = 23
#
# db = pymysql.connect(host=host, port=port, user=username, password=password, db=db_name)
# cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, name, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

# mysql4
# import pymysql
# username = 'root'
# password = 'chenze'
# host = 'localhost'
# port = 3306
# db_name = 'spiders'
#
# id = '2009003'
# name = 'xiaoma'
# age = 23
#
# db = pymysql.connect(host=host, port=port, user=username, password=password, db=db_name)
# cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, name, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

# mysql5
import pymysql
username = 'root'
password = 'chenze'
host = 'localhost'
port = 3306
db_name = 'spiders'

db = pymysql.connect(host=host, port=port, user=username, password=password, db=db_name)
cursor = db.cursor()
sql = 'SELECT * FROM students'
cursor.execute(sql)
print(cursor.rowcount)
one = cursor.fetchone()
db.close()


# mongo 1
# import pymongo
# from bson.objectid import ObjectId
#
# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client.test
# collection = db.students
#
# student = {
#     'id': '20090705',
#     'name': 'hanson',
#     'age': 28,
#     'gender': 'man'
# }
# result = collection.insert(student)
#
# result = collection.find_one({'name': 'hanson'})
# print(type(result))
# print(result)
#
# result = collection.find_one({'_id': ObjectId('5c04d376a17fdd17784fd7d2')})
# print(result)


# redis 1
# from redis import StrictRedis
#
# redis = StrictRedis(host='localhost', port=6379, db=0)
# redis.set('name', 'hanson')
# print(redis.get('name'))

