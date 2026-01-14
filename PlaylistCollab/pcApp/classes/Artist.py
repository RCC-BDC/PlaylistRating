from json import dumps

class Artist:
    name = ""
    genre = ""
    followers = 0
    popularity = 0
    image = ""

    def __init__(self):
        return

    def toJSON(self):
        return dumps(self, default=lambda obj : obj.__dict__)

