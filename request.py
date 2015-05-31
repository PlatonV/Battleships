import urllib2

def request(x, y):
    g=str(chr(x+ord('A')-1))
    conn = urllib2.urlopen("http://battleship.pitechplus.com/live/game/shoot/teamiqwycvqd?coordinates=" + g + str(y))
    return conn.read(100)
