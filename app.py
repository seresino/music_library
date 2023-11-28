from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.album import Album


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

# Retrieve all albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

# List them out
for album in albums:
    print(album)

found_album = album_repository.find(1)
print(f"Found: {found_album}")

new_album = Album(None, 'Arrival', 1976, 2)
album_repository.create(new_album)
all_albums = album_repository.all()
for album in all_albums:
    print(album)

album_repository.delete(1)
reduced_albums = album_repository.all()
for album in reduced_albums:
    print(album)