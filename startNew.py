import urllib2

def startNewGame():
    conn = urllib2.urlopen("http://battleship.pitechplus.com/game/start_new_game/team{teamId}")
    print conn.read(100)

startNewGame()
