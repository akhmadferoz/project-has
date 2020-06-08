'''
This is the source code for the back end of the game
'''
import random

# --------------- Stack Commands ---------------------------------------------
def push(lst,x):
    lst.append(x)

def pop(lst):
    return lst.pop()

def top(lst):
    return lst[-1]

def is_empty(lst):
    if len(lst)==0:
        return True
    return False
# --------------- Queue Commands ---------------------------------------------
def Enqueue(lst, x, p):
    tup = (x, p)
    if len(lst) == 0:
        return lst.append(tup)
    else:
        for i in range(len(lst)):
            if lst[i][1] < p:
                lst.insert(i, tup)
                return lst
            elif lst[i][1] == p:
                if lst[i][0] > x:
                    lst.insert(i, tup)
                    return lst
                else:
                    lst.insert(i+1, tup)
                    return lst
    lst.append(tup)

def front(lst):
    return lst[0]

def Dequeue(lst):
    p = lst.pop(0)
    return p[0]

