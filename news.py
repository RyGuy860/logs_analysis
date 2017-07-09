#!/usr/bin/env python

import psycopg2

dbname = "news"


def get_popularArticles():
    """ Returns the three most popular articels of all time."""
db = psycopg2.connect("dbname=news")
c = db.cursor()

c.execute(
    "select title, views from "
    " (select path, count(*) as views from log group by path)"
    "as log join "
    " articles on log.path like concat('%', articles.slug) "
    " order by views desc limit 3;")

articlesResults = c.fetchall()
print("The three most popular articels of all time")
for i in articlesResults:
    print (i[0] + ' | ' + str(i[1]) + ' ' + 'views')

db.close()
print("\n")


def get_popularAuthors():
    """ Returns the most popular article authors of all time"""
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(
    "select name, count(*) as views from authors "
    " join articles on articles.author = authors.id join "
    " log on log.path like concat ('%', articles.slug) group by "
    " name order by views desc;")

authorResults = c.fetchall()
print("The most popular article authors of all time")
for i in authorResults:
        print (i[0] + ' | ' + str(i[1]) + ' ' + 'views')

db.close()
print("\n")


def get_daysWithMostRequestErrors():
    """ Return the days where more than 1% of request lead to errors"""
db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(
    "select to_char(total_requests.date, 'FMMonth DD, YYYY'), "
    " round((num_total - num_ok) * 100.0 / num_total, 1) "
    "as num_errors from total_requests, ok_requests where "
    "total_requests.date = ok_requests.date "
    " and (num_total - num_ok) * 100.0 / num_total > 1 "
    "order by num_errors desc;")

requestResults = c.fetchall()
print("The days where more than 1 percent of request lead to errors")
for i in requestResults:
    print(i[0] + ' | ' + str(i[1]) + '%')

db.close()
