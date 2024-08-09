import sqlite3
from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields


def execute_query(query, args=()):
    with sqlite3.connect('chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()

    return records

app = Flask(__name__)

@app.route("/order-price")
@use_kwargs(
    {
        "country" : fields.Str(
            missing = ""
        )
    },
    location="query"
)
def order_price(country):
    query = (f"SELECT Sum(UnitPrice * Quantity), invoices.BillingCountry "
            f"FROM invoice_items JOIN invoices ON "
            f"invoice_items.InvoiceId = invoices.InvoiceId "
            f"GROUP BY invoices.BillingCountry ")
    if country != "":
        query += f"HAVING invoices.BillingCountry=\"{country}\";"

    data = execute_query(query=query)
    result = ""
    for country_sales in data:
        result += f"{country_sales[1]}: {country_sales[0]} sales<p>"

    return result


@app.route("/get-info-about-track")
@use_kwargs(
    {
        "track_ID" : fields.Str(
            missing = 0
        )
    },
    location="query"
)
def get_all_info_about_track(track_ID):
    query = ("SELECT TrackId, Name AS artist, Title, name_art, genres, Composer, "
             "playlists, Milliseconds, Bytes, media_type "
             "FROM artists JOIN albums ON albums.ArtistId=artists.ArtistId "
             "JOIN (SELECT Name AS name_art, Bytes, UnitPrice, Composer, Milliseconds,"
             "AlbumId, GenreId, MediaTypeId,TrackId  FROM tracks) AS tracks  ON tracks.AlbumId = albums.AlbumId "
             "JOIN (SELECT Name AS genres, GenreId FROM genres) AS genres ON genres.GenreId= tracks.GenreId "
             "JOIN (SELECT Name AS media_type, MediaTypeId FROM media_types) as mt ON mt.MediaTypeId = tracks.MediaTypeId "
             "JOIN (SELECT Name AS playlists, TrackId AS tid FROM playlists p "
             "JOIN playlist_track pt  ON p.playlistId=pt.playlistId) as pl "
             "ON pl.tid = tracks.TrackId GROUP BY TrackId, playlists "
             f"HAVING TrackId LIKE {track_ID};")

    """1. track_ID,2. artist,3. albums,4. name art,5. genres,
    6. composer,7. playlists,8. milliseconds, 9.bytes, 10.media type"""
    data = execute_query(query=query)

    playlists = ""
    for row in data:
        playlists += f"{row[6]}, "
    playlists = playlists[:-2]

    result = (f"Track ID: {track_ID}<p>"
              f"Artist: {data[0][1]}<p>"
              f"Album: {data[0][2]}<p>"
              f"Name art: {data[0][3]}<p>"
              f"Genres: {data[0][4]}<p>"
              f"Composer: {data[0][5]}<p>"
              f"Playlists: {playlists}<p>"
              f"Seconds: {data[0][7]/1000}<p>"
              f"KB: {round(data[0][8]/1000)}<p>"
              f"Media type: {data[0][9]}<p>")
    

    return result



if __name__ == "__main__":
    app.run(
        port=5000
    )

