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
# id = '2009005'
# name = 'chenze'
# age = 28
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
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'hanson')
print(redis.get('name'))
