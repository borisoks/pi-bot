
BOARD = "BOARD"
OUT = "OUT"
LOW = "LOW"
HIGH = "HIGH"

def log(m):
    print("mock_GPIO." + m)
 
def setwarnings(b):
    print("setwarnings(" + str(b) + ")")

def setmode(b):
    print("setmode(" + str(b) + ")")

def setup(p, d, initial):
    print("setup(" + str(p) + ", " + str(d) + ", " + str(initial) + ")")

def output(p, v):
    print("output(" + str(p) + ", " + str(v) + ")")
