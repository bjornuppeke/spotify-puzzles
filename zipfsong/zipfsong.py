#!/usr/bin/env python

import sys

class InvalidInputException(Exception):
    pass

def zipf(i, f):
    return i * f

def parse_song(raw_song):
    """Return tuple of a parsed song line

    >>> parse_song("197812 re_hash")
    (197812, 're_hash')

    """
    try:
        bits = raw_song.split()
        f = int(bits[0])
        s = bits[1].rstrip()
    except (ValueError, IndexError), e:
        raise InvalidInputException()
    return f, s

def weigh_song(i, f, s):
    """Return tuple of a song with zipfs law applied

    >>> weigh_song(1, 0, 30, "lol")
    (30, 'lol')

    """
    q = zipf(i + 1, f)
    return q, s

def ordered_songs(m, songs):
    """Return sorted list of `m` number of tuples, sorted by `q` and `i`

    >>> ordered_songs(2, [(60, "abc"), (30, "def"), (10, "ghi")])
    [(60, 'abc'), (60, 'def')]

    """
    songs = [weigh_song(i, f, s) for i, (f, s) in enumerate(songs)]
    return sorted(songs, key=lambda song: song[0], reverse=True)[:m]

def process(source):
    try:
        n, m = map(int, source.readline().split())
    except ValueError:
        raise InvalidInputException()
    return ordered_songs(m, map(parse_song, list(source)[:n]))

def string_list(tuples):
    """Return string representation of a list of tuples

    >>> string_list([(60, 'abc'), (60, 'def')])
    'abc\\ndef'

    """
    return "\n".join([s for q, s in tuples])

if __name__ == "__main__":
    print string_list(process(sys.stdin))