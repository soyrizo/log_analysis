#!/usr/bin/env python3
#
# Spencer Stenger
# Log Analysis Assignment
#
# A log analysis tool for reporting.

#from logdb import popular_three_articles, popular_authors, log_errors
import datetime, psycopg2

# Questions one through three
POPULAR_ARTICLES = '''
What are the most popular three articles of all time?\
'''
POPULAR_AUTHORS = '''
Who are the most popular article authors of all time?\
'''
LOG_ERRORS = '''
On which days did more than 1% of requests lead to errors?\
'''

# Format pattern for questions 1 and 2
VIEWS = '''● %s — %s views\n'''

# Format pattern for question 3
LOG_ERROR = '''● %s — %s%% errors\n'''

# Database name to connect to
DBNAME = "news"

# queries for most popular three articles of all time
def popular_three_articles():
    # attempt to query for most popular three articles
    try:
        # connect to database
        connection = psycopg2.connect(database=DBNAME)
        # initiate cursor
        cursor = connection.cursor() 
        # PSQL query
        select_contents = "select articles.title, count(log.path) as num\
            from articles, log\
            where articles.slug = right(log.path, -9)\
            group by articles.title\
            order by num\
            desc limit 3"
        # execute query
        cursor.execute(select_contents)
        # return all results
        return cursor.fetchall()
        # close db connection
        connection.close()
    # throw an error if any part of the db work fails
    except:
        print("Error calculating popular three articles.")


# queries for most popular authors of all time
def popular_authors():
    try:
        connection = psycopg2.connect(database=DBNAME)
        cursor = connection.cursor()
        select_contents = "select authors.name, count(log.path) as num\
            from articles, log, authors\
            where articles.slug = right(log.path, -9)\
            and authors.id = articles.author\
            group by authors.name\
            order by num desc"
        cursor.execute(select_contents)
        return cursor.fetchall()
        connection.close()
    except:
        print("Error calculating popular authors.")


# queries for days where more than 1% of requests lead to errors
def log_errors():
    try:
        connection = psycopg2.connect(database=DBNAME)
        cursor = connection.cursor()
        select_contents = "SELECT date, ROUND((percent * 100), 1)\
            FROM\
            (SELECT DATE(time) AS date,\
            ROUND(\
            CAST(\
            SUM(\
            CASE WHEN status LIKE '40%' THEN 1 ELSE 0 END)::float/\
            COUNT(status)::float AS numeric), 3) AS percent\
            FROM log GROUP BY date) AS errorTable\
            WHERE percent > '0.01'"
        cursor.execute(select_contents)
        return cursor.fetchall()
        connection.close()
    except:
        print("Error calculating request errors.")


def answer_one():
    '''Answer to question one, most popular three articles of all time.'''
    print(POPULAR_ARTICLES)
    answer_1 = "".join(VIEWS % (title, num) for title, num in popular_three_articles())
    print(answer_1)


def answer_two():
    '''Answer to question two, most popular authors of all time.'''
    print(POPULAR_AUTHORS)
    answer_2 = "".join(VIEWS % (author, num) for author, num in popular_authors())
    print(answer_2)


def answer_three():
    '''Answer to question three, which day had > 1% of request errors.'''
    print(LOG_ERRORS)
    answer_3 = "".join(LOG_ERROR % (date, errors) for date, errors in log_errors())
    print(answer_3)


def main():
    answer_one()
    answer_two()
    answer_three()


if __name__ == '__main__':
    main()


