import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
import csv

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#get songs from the Pop Connoisseur Playlist

pl_id = 'spotify:playlist:5AvWMqi0lbzSPvDR6WWesu'
offset = 0

while True:
    response = sp.playlist_tracks(pl_id, offset=offset, fields='items.track.id,total')
    pc_tracks = [x['track']['id'] for x in response['items']]
    print(pc_tracks)
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])
    s = 0
    with open('popconn.csv', 'w', newline='') as csvfile:
        fieldnames = ['song_id']
        thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        thewriter.writeheader()
        for song in pc_tracks:
            s += 1
            thewriter.writerow({'song_id': song})

    if len(response['items']) == 0:
        break

#get songs from the Billboard Hot 100

pl_id2 = 'spotify:playlist:6UeSakyzhiEt4NB3UAd6NQ'
offset = 0

while True:
    response = sp.playlist_tracks(pl_id2, offset=offset, fields='items.track.id,total')
    bb_tracks = [x['track']['id'] for x in response['items']]
    print(bb_tracks)
    offset = offset + len(response['items'])
    print(offset, ",", response['total'])
    with open('bb.csv', 'w', newline='') as csvfile:
        fieldnames = ['song_id']
        thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        thewriter.writeheader()
        for song in bb_tracks:
            s += 1
            thewriter.writerow({'song_id': song})
    if len(response['items']) == 0:
        break
