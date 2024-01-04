# Varianta A - pocitejme, ze 0 je cislo kladne. / takze vlastne isNonNegative, ale budiz :)

def isPositive(n):
    if n >= 0:
        return True
    else:
        return False
    
print(isPositive(-4))
print(isPositive(0))
print(isPositive(5))

# Varianta B

import turtle

def drawTriangle(length):
    t = turtle.Turtle()
    t.speed(1)
    for _ in range(3):
        t.forward(length)
        t.left(120)
    turtle.done() # done dela, ze okno nezhasne okamzite po skonceni

drawTriangle(300)

# Varianta C

def findDuplicates(words):
    duplicates = []
    uniqueWords = []
    
    for word in words:
        if word in uniqueWords:
            duplicates.append(word)
        else:
            uniqueWords.append(word)
    
    return list(set(duplicates)) # odstranuje duplicity v duplicitach, asi by slo proste setnout uz prvotni uniqueWords, ale na to jsem extremne lina to ted prepisovat :D

words = ["Green", "Blue", "Red", "Blue", "Yellow", "Blue", "Red"]
print(findDuplicates(words))
unikatky = ["Red", "Green", "Blue"]
print(findDuplicates(unikatky))