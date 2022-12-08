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
    print(c.fetchall())

# links created before Sep 1, 1993
def links_before_sep1():
    query = """SELECT user_id
            FROM follows
            WHERE date < '1993-09-01'
    """
    c.execute(query)
    print(c.fetchall())

# first name of links created before Sep 1, 1993
def links_before_sep1_first():
    query = """SELECT u.first_name, f.date
            FROM follows f
            JOIN users u ON u.user_id = f.user_id
            WHERE f.date<'1993-09-01'
    """
    c.execute(query)
    print(c.fetchall())

#  how many people followed each user as of 1999-12-31. users full name, number of followers
def followers_per_user():
    query = """SELECT u.first_name, u.last_name, COUNT(f.follows)
            FROM follows f
            JOIN users u on u.user_id = f.user_id
            WHERE f.date > '1999-12-31'
            GROUP BY f.user_id
        """
    c.execute(query)
    print(c.fetchall())

# how many followers per
def following():
    query = """SELECT user_id, COUNT(*)
            FROM follows
            GROUP BY user_id
    """
    c.execute(query)
    print(c.fetchall())

# all rows where someone from one house follows someone from another house, user names
def diff_house():
    query = """SELECT u1.first_name, u1.house, u2.first_name, u2.house
            FROM follows f
            JOIN users u1 on u1.user_id = f.user_id
            JOIN users u2 on u2.user_id = f.follows
            WHERE NOT u1.house == u2.house
    """
    c.execute(query)
    print(c.fetchall())

# unrequited followings
def unrequited():
    query = """SELECT f.user_id, f.follows
            FROM follows f
            LEFT JOIN follows f2 ON f.follows = f2.user_id AND f.user_id = f2.follows
            WHERE f2.user_id IS NULL
    """
    c.execute(query)
    print(c.fetchall())

unrequited()
