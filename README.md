# Book Storm
You are building a backend service and a database for a book store platform, with the following 2 raw datasets:

## Book Store data
Link: [data/book_store_data.json](data/book_store_data.json)

This dataset contains a list of book store with their books and prices, as well as their cash balances. This cash balance is the amount of money the book store hold in their merchant accounts on this platform. It increases by the respective book price whenever a user purchases a book from them.

## User data
Link: [data/user_data.json](data/user_data.json)

This dataset contains a list of users with their transaction history and cash balances. This cash balance is the amount of money the users hold in their wallets on this platform. It decreases by the book price whenever they purchase a book.

These are all raw data, which means that you are allowed to process and transform the data, before you load it into your database.


# Project Setup
* pip install pipenv
* pipenv --three 
* python -m pipenv shell (in virtual env)
* pip install - r requirements.txt
* gunicorn --bind 0.0.0.0:8000 myproject.wsgi

Then, open (Site Domain):8000

# Docker setup
* install docker (sudo apt install docker.io)
* sudo docker-compose build
* sudo docker-compose run web python src/manage.py migrate
* sudo docker-compose up
# Deploy by heroku
https://fierce-shelf-22652.herokuapp.com/bsname_bookname_bookprice_username/list/0/
# API doc
![圖片](https://user-images.githubusercontent.com/32931993/130922866-ab335886-79ad-45af-87ed-539fce85654f.png)


# The Task
The task is to build an API server, with documentation and a backing relational database that will allow a frontend client to navigate through that sea of data easily, and intuitively. The frontend team will later use that documentation to build the frontend clients.

The operations the frontend team would need you to support are:

* List all book stores that are open at a certain datetime
* List all book stores that are open on a day of the week, at a certain time
* List all book stores that are open for more or less than x hours per day or week
* List all books that are within a price range, sorted by price or alphabetically
* List all book stores that have more or less than x number of books
* List all book stores that have more or less than x number of books within a price range
* Search for book stores or books by name, ranked by relevance to search term
* The top x users by total transaction amount within a date range
* The total number and dollar value of transactions that happened within a date range
* Edit book store name, book name, book price and user name
* The most popular book stores by transaction volume, either by number of transactions or transaction dollar value
* Total number of users who made transactions above or below $v within a date range
* Process a user purchasing a book from a book store, handling all relevant data changes in an atomic transaction

In your repository, you would need to document the API interface, the commands to run the ETL (extract, transform and load) script that takes in the raw data sets as input, and outputs to your database, and the command to set up your server and database. You may use docker to ensure a uniform setup across environments.


