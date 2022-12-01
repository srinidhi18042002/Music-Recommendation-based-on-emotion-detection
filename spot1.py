import json
import spotipy
import webbrowser

username = '31cchxgdh45tnavy35ziploaarma'
clientID = '294b1e94fffb4a109716de0e90c19a69'
clientSecret = 'b38ab9841dfa4373aa541b16e1701a41'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()
def get_song(search_song):
    results = spotifyObject.search(search_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)

#get_song("Believer")

