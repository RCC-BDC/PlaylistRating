from json import dumps

class Track:

    def __init__(self):
        self.name = ""
        self.album = ""
        self.artists = []
        self.popularity = 0
        self.image = ""
        return

    def toJSON(self):
        return dumps(self, default=lambda obj : obj.__dict__)

