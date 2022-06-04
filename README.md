# Recommendation system

Item Based Collaborative filtering for online book store

## Technologies

Project is created with:
* Python version: 3.10.2
* Flask version: 2.0.2
* MongoDB version: 5.0.8

## Setup
To run this project, install it locally using pip:

```bash
pip install flask
pip install flask_cors pymongo
pip install flask-restx
```

## Run
To run this project, run the calculation_controller file

## Files

* seed_data: Jupiter notebook with seeding data functionality
* calculation_controller: Flask controller file
* calculation_bll: Business layer (all main calculations)
* calculation_utils: File with additional functions
* calculation_dal: Data access functionality
* google_books_1299: CSV file with books to seed the database
* users: JSON file with users to seed the database
