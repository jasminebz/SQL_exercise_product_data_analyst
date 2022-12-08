import sqlite3
import pandas as pd

# connect to sqlite db
conn = sqlite3.connect("data.sqlite")
c = conn.cursor()


# how many users in each house?
def users_per_house():
    query = """SELECT house, COUNT(*)
            FROM users
            GROUP BY house"""

    c.execute(query)
    count = c.fetchall()
    print(count)

# links created before Sep 1, 1993
def links_before_sep1():
    query = """SELECT user_id
            FROM follows
            WHERE date < '1993-09-01'
    """
    c.execute(query)
    count = c.fetchall()
    print(count)

# first name of links created before Sep 1, 1993
def links_before_sep1_first():
    query = """SELECT u.first_name, f.date
            FROM follows f
            JOIN users u ON u.user_id = f.user_id
            WHERE f.date<'1993-09-01'
    """
    c.execute(query)
    count = c.fetchall()
    print(count)

#  how many people followed each user as of 1999-12-31. users full name, number of followers
def followers_per_user():
    query = """SELECT u.first_name, u.last_name, COUNT(f.follows)
            FROM follows f
            JOIN users u on u.user_id = f.user_id
            WHERE f.date > '1999-12-31'
            GROUP BY f.user_id
        """
    c.execute(query)
    count = c.fetchall()
    print(count)

# how many followers per
def following():
    query = """SELECT user_id, COUNT(*)
            FROM follows
            GROUP BY user_id
    """
    c.execute(query)
    count = c.fetchall()
    print(count)

following()
