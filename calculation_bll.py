from calculation_dal import *
from calculation_utils import *

def calculate_similarity():
    new_rates = get_rates_for_previous_day()

    requests = {}    
    yesterday_datetime = datetime.datetime.utcnow() - datetime.timedelta(days = 1)
    yesterday = datetime.datetime(yesterday_datetime.year, yesterday_datetime.month, yesterday_datetime.day)

    print(new_rates)

    for rate in new_rates: 
        for review in rate['reviews']:
            if (review['createdAt'] == yesterday):
                if (rate['bookId'] in requests.keys()):
                    requests[rate['bookId']].append(review['userId'])
                else:
                    requests[rate['bookId']] = [review['userId']]   

    books_to_delete_similarities = [item['bookId'] for item in new_rates]
    delete_similarity_by_books(books_to_delete_similarities)

    new_similaritites = []

    for book in new_rates:
        books_to_compare = get_rates_by_users(requests[book['bookId']])

        book_reviews = change_scheme_user_rate(book)

        for other in books_to_compare:
            if other['bookId'] != book['bookId']:
                if any(other['bookId'] in item.keys() and book['bookId'] in item.keys() for item in new_similaritites):
                    continue

                scope = koef_pearson(book_reviews, other)
                similarity = {
                    'book1':book['bookId'],
                    'book2':other['bookId'],
                    'similarity':scope
                    }
                new_similaritites.append(similarity)

    insert_books_similarity(new_similaritites)
    return len(new_similaritites)
       
def calculate_recomendations_by_book(book_id):    
    book_similarities = get_similarity_by_book(book_id)

    similarities = []
    for item in book_similarities:
            similarities.append((item['similarity'], item['book1'] if item['book1'] != book_id else item['book2']))
            
    similarities.sort()
    similarities.reverse()
    return similarities