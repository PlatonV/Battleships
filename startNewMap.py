import urllib2

def startNewMap(prompt = 0):
    conn = urllib2.urlopen("http://battleship.pitechplus.com/game/start_new_map/team9321")
    
    if prompt == 1:
        print(conn.read(100))

if __name__ == "__main__":
    startNewMap(1)
    raw_input("Press enter to continue...")
