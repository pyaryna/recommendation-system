import datetime

database = None

def connect_to_database(db):
    global database
    database = db

def get_collection(dataset):
    cursor = database[dataset].find({})
    return list(cursor)

def get_rates_for_previous_day():    
    yesterday_datetime = datetime.datetime.utcnow() - datetime.timedelta(days = 1)
    yesterday = datetime.datetime(yesterday_datetime.year, yesterday_datetime.month, yesterday_datetime.day)
    cursor = database.rates.find({'reviews.createdAt':{ '$eq': yesterday}})
    return list(cursor)

def get_rates_by_users(users):
    cursor = database.rates.find({
        'reviews.userId' : { '$in' : users}
    })
    return list(cursor)    

def get_similarity_by_book(bookId):
    cursor = database.similarity.find({
        '$or': [
            {'book1' : bookId},
            {'book2' : bookId}
        ]})
    return list(cursor)

def delete_similarity_by_books(bookIds):
    database.similarity.delete_many({
        '$or': [
            {'book1' : { '$in' : bookIds}},
            {'book2' : { '$in' : bookIds}}
        ]})

def insert_books_similarity(similarity):
    database.similarity.insert_many(
        [ i for i in similarity])  
