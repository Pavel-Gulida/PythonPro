from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields
import sqlite3
#1
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y


class Circle:
    def __init__(self, radius):
        self.radius=radius
    def contains(self, p: Point):
        if p.x ** 2 + p.y ** 2 <= self.radius ** 2:
            return True
        return False

circle = Circle(5)
print(circle.contains(Point(3,4)))
print(circle.contains(Point(0,0)))
print(circle.contains(Point(0,6)))

#2
app = Flask(__name__)

def execute_query(query, args=()):
    with sqlite3.connect('chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()

    return records

@app.route("/")
@use_kwargs(
    {
        "genre": fields.Str(
            missing = ""
        )
    },
    location="query"
)
def stats_by_city(genre):
    query = ("SELECT COUNT(Name), Name, BillingCity, BillingCountry "
             "FROM invoice_items ii JOIN invoices i ON ii.InvoiceId=i.InvoiceId "
             "JOIN (SELECT TrackId,GenreId  FROM tracks) AS t ON t.TrackId = ii.TrackId "
             "JOIN genres g ON g.GenreId = t.GenreId "
             f"GROUP BY BillingCity HAVING g.Name = \"{genre}\"")

    if genre == "":
        return "Enter genre."

    genres = execute_query(query="SELECT Name FROM genres")
    exists_genre = False
    for row in genres:
        if genre == row[0]:
            exists_genre = True
    if not exists_genre:
        return "This genre doesn't exist."

    '''1. Count genre,2. genre,3. city,4. country'''
    data = execute_query(query=query)
    Max = 0
    for row in data:
       if row[0] > Max:
           Max = row[0]
    result = f"{genre}:<p>"
    for row in data:
        if row[0] == Max:
            result += f"{row[2]}, {row[3]}<p>"

    return result


if __name__ == "__main__":
    app.run(
        port=5000
    )
