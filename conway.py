import random, time, copy
WIDTH = 20
HEIGHT = 8

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append('_')
    nextCells.append(column)

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            livingNeighbors = 0
            if y != 0:
                if x != 0:
                    if currentCells[leftCoord][aboveCoord] == '#':
                        livingNeighbors += 1
                if currentCells[x][aboveCoord] == '#':
                    livingNeighbors += 1
                if x != WIDTH-1:
                    if currentCells[rightCoord][aboveCoord] == '#':
                        livingNeighbors += 1
            if x != 0:
                if currentCells[leftCoord][y] == '#':
                    livingNeighbors += 1
            if x != WIDTH-1:
                if currentCells[rightCoord][y] == '#':
                    livingNeighbors += 1
            if y != HEIGHT-1:
                if x != 0:
                    if currentCells[leftCoord][belowCoord] == '#':
                        livingNeighbors += 1
                if currentCells[x][belowCoord] == '#':
                    livingNeighbors += 1
                if x != WIDTH-1:
                    if currentCells[rightCoord][belowCoord] == '#':
                        livingNeighbors += 1
            
            if currentCells[x][y] == '#' and (livingNeighbors == 2 or livingNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '_' and livingNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = '_'
    time.sleep(1)