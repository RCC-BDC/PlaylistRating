

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

