import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist('Caamp')
artist_repository.save(artist1)

artist2 = Artist('Hilltop Hoods')
artist_repository.save(artist2)

artist_repository.select_all()


album_1 = Album("Pineapples","Indie", artist1,)
album_repository.save(album_1)

album_2 = Album("Nosebleed section", "Aussie hop", artist2,)
album_repository.save(album_2)

for album in album_repository.select_all():

    print(album.__dict__)
pdb.set_trace()
