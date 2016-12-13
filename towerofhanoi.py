def moveTower(height, source, dest, temp):
    if height >= 1:
        moveTower(height-1, source, temp, dest)
        moveDisk(source, dest)
        moveTower(height-1, temp, dest, source)

def moveDisk(source, dest):
    print("moving disk from", source ,"to", dest)

moveTower(3,"A","B","C")

