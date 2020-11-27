import sys
sys.setrecursionlimit(10)
i = 0
def fname():
    global i
    i = i + 1
    print("bibin", i)
    fname()

fname()