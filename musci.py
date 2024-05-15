def make_album(artist_name, album_title, num_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

# Three dictionaries representing different albums
album1 = make_album("Taylor Swift", "Fearless")
album2 = make_album("Ed Sheeran", "÷ (Divide)", 12)
album3 = make_album("Beyoncé", "Lemonade")

# Print each dictionary to show the album information
print(album1)
print(album2)
print(album3)
