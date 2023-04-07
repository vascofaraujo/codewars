import re

def song_decoder(song):
    output = re.sub("(WUB)+", " ", song)

    return output.strip()
