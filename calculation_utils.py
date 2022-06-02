import math

def koef_pearson(book1_reviews, book2):
    users = []
    
    book2_reviews = change_scheme_user_rate(book2)   

    for item in book1_reviews: 
        if item in book2_reviews: 
            users.append(item)

    n = len(users)
    if n == 0: 
        return 0   

    avg1 = sum([book1_reviews[it] for it in users]) / n
    avg2 = sum([book2_reviews[it] for it in users]) / n  
    

    num = 0 
    sq_sum1 = 0
    sq_sum2 = 0

    for it in users:
        num += (book1_reviews[it] - avg1) * (book2_reviews[it] - avg2)
        sq_sum1 += pow((book1_reviews[it] - avg1), 2)
        sq_sum2 += pow((book2_reviews[it] - avg2), 2)

    den = math.sqrt(sq_sum1 * sq_sum2)
    if den == 0: 
        return 0

    r = ((num / den) + 1) / 2
    return round(r, 3)

def change_scheme_user_rate(rate):
    new_reviews = {}
    for review in rate['reviews']:
        new_reviews[review['userId']] = review['rate']

    return new_reviews