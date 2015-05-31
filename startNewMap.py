import urllib2

def startNewMap(prompt = 0):
    conn = urllib2.urlopen("http://battleship.pitechplus.com/live/game/start_new_map/teamiqwycvqd")
    
    result = conn.read(100)

    if prompt == 1:
        print(result)

    return result

if __name__ == "__main__":
    startNewMap(1)
    raw_input("Press enter to continue...")
