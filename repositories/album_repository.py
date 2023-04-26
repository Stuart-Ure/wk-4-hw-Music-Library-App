from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def delete_all ():
    sql = "DELETE FROM albums"
    run_sql(sql)


def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    print (results)
    id = results[0]['id']
    album.id = id
    return album

def select_(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album (result['title'], result['genre'], artist, result[id])
    return album

def select_all():
    album = []
    sql = "SELECT * FROM album"
    results = run_sql(sql)

    for row in results:
        album = Album(results['title'],results['genre'], results['artist_id'])
        album.append(album)
    return album
