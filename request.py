import urllib2

def request(x, y):
    conn = urllib2.urlopen("http://battleship.pitechplus.com/game/shoot/team9321?coordinates=" + str(x) + str(y))
    return conn.read(100)
