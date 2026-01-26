from .classes import Artist, Track
from json import dumps

def parseTopArtists(respObj):
    # Iterate over each result returned
    items = respObj.get('items')
    artistDataList = []
    for artist in items:
        # genres, images, name, followers
        artistObj = Artist.Artist()
        artistObj.name = artist.get('name')
        artistObj.genre = artist.get('genres')[0]
        artistObj.followers = artist.get('followers').get('total')
        artistObj.popularity = artist.get('popularity')
        artistObj.image = artist.get('images')[0].get('url')
        print(artist.get('images'))

        # Need to convert trackObj to string before adding to list
        artistDataList.append(artistObj.toJSON())

    return artistDataList

def parseLink(link):
    spotifyKeyWord = link.find("spotify")
    if spotifyKeyWord == -1:
        print("Needs to be spotify link")
        return
    elif spotifyKeyWord != 13:
        print("Issue with link")
        return
    playlistKeyword = link.find("playlist")
    playlistKeyword = playlistKeyword + 9
    questionmarkPos = link.find("?")
    playlistId = link[playlistKeyword:questionmarkPos]

    print(playlistId)
    return playlistId


def parseTopTracks(respObj):
    # Get album, album cover, artist, track, and popularity
    items = respObj.get('items')
    tracksList = []
    # Increment over each track
    for track in items:
        trackObj = Track.Track()
        for artist in track.get('artists'):
            artistName = artist.get('name')
            trackObj.artists.append(artistName)
        trackObj.album = track.get('album').get('name')
        trackObj.name = track.get('name')
        trackObj.image = track.get('album').get('images')[1].get('url')
        trackObj.popularity = track.get('popularity')

        # Need to convert trackObj to string before adding to list
        tracksList.append(trackObj.toJSON())

    return tracksList


def parsePlaylistReturn(playlist_dict):
    items = playlist_dict.get("tracks")
    #print(items.get("items")[0])
    return items

