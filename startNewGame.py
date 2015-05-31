import urllib2

def startNewGame(prompt = 0):
    conn = urllib2.urlopen("http://battleship.pitechplus.com/live/game/start_new_game/teamiqwycvqd")

    if prompt == 1:
        print(conn.read(100))

if __name__ == "__main__":
    startNewGame(1)
    raw_input("Press enter to continue...")
