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