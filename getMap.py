import urllib2
import sys

def char_range(c1, c2):
    for c in xrange(ord(c1), ord(c2)):
        yield chr(c)

f = open("matrix.txt", "w")

if len(sys.argv) == 2:
    filename = sys.argv[1]
    f = open(filename, 'w')

for i in range(1, 11):
    for j in char_range('A', 'K'):
        print("Requesting: " + str(j) + str(i))
        url = "http://battleship.pitechplus.com/game/shoot/team9321?coordinates=" + str(j) + str(i) 
        conn = urllib2.urlopen(url)
        
        response = conn.read(100)
        print(response)

        if response == "MISS":
            f.write("0")
        elif response == "HIT":
            f.write("1")
        elif response == "DESTROYED":
            f.write("2")

    f.write("\n")

