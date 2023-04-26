from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

import repositories.album_repository as album_repository


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all ():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select_(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist (result['name'], result[id])
    return artist

def select_all():
    artist= []


def select_all():
    artist = []

sql = "SELECT * FROM artist"
results = run_sql(sql)

for row in results:
    artist = Artist(results['name'],results['id'] )
    artist.append(artist)
    return artist