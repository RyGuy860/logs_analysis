import psycopg2

dbname = "news"

def get_popularArticles():
	""" Returns the three most popular articels of all time."""
	db = psycopg2.connect("dbname=news")
	c = db.cursor()
	c.execute("select title, count(*) as views from log join " 
			  " articles on log.path like concat('%', articles.slug) "
			  " group by title order by views desc limit 3;") 
	articlesResults = c.fetchall()
	for i in articlesResults:
		print (i[0] + ' | ' + str(i[1]))
	
	db.close()

	return articlesResults

def get_popularAuthors():
	""" Returns the most popular article authors of all time"""
	db = psycopg2.connect("dbname=news")
	c = db.cursor()
	c.execute("select name, count(*) as views from authors "
	 		  " join articles on articles.author = authors.id join " 
	 		  " log on log.path like concat ('%', articles.slug) group by " 
	 		  " name order by views desc;")
	authorResults = c.fetchall()
	for i in authorResults:
		print (i[0] + ' | ' + str(i[1]))

	db.close()

	return authorResults

def get_daysWithMostRequestErrors():
	""" Return the days where more than 1% of request lead to errors"""
	db = psycopg2.connect("dbname=news")
	c = db.cursor()
	c.execute("select to_char(total_requests.date, 'FMMonth DD, YYYY'), "
			  " trunc((num_total - num_ok) * 100.0 / num_total, 1) as num_errors from "
			  " total_requests, ok_requests where total_requests.date = ok_requests.date "
			  " and (num_total - num_ok) * 100.0 / num_total > 1 order by num_errors desc;")
	requestResults = c.fetchall()
	for i in requestResults:
		print(i[0] + ' | ' + str(i[1]))

	db.close()

	return requestResults


print("The three most popular articels of all time")
get_popularArticles()
print("\n")

print("The most popular article authors of all time")
get_popularAuthors()
print("\n")

print("The days where more than 1 percent of request lead to errors")
get_daysWithMostRequestErrors()
print("\n")