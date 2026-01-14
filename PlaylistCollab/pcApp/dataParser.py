from .classes import Artist
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
        artistObj.image = artist.get('images')[1].get('url')
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


def parsePlaylistReturn(playlist_dict):
    items = playlist_dict.get("tracks")
    #print(items.get("items")[0])
    return items

