# Book Storm
You are building a backend service and a database for a book store platform, with the following 2 raw datasets:

## Book Store data
Link: [data/book_store_data.json](data/book_store_data.json)

This dataset contains a list of book store with their books and prices, as well as their cash balances. This cash balance is the amount of money the book store hold in their merchant accounts on this platform. It increases by the respective book price whenever a user purchases a book from them.

## User data
Link: [data/user_data.json](data/user_data.json)

This dataset contains a list of users with their transaction history and cash balances. This cash balance is the amount of money the users hold in their wallets on this platform. It decreases by the book price whenever they purchase a book.

These are all raw data, which means that you are allowed to process and transform the data, before you load it into your database.

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

## Bonus
This is optional, and serves as additional proof points. We will consider it complete even without this functionality

Write appropriate tests with an appropriate coverage report.

## Deployment
It'd be great if you can deploy this on the free tier of any cloud hosting platform (eg. free dyno on Heroku), so that we can easily access the application via an url.

# About Response
* Fork this repository to your github account.
* Add redtear1115 as collaborator to your private repository.
* Write a introduction to all your works on following link.
  * Link: [response.md](response.md) (Current contest as an example. Feel free to edit/remove it.)
