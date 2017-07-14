# Flood fill algorithm


# to create an example with
def makeGrid(width, height):
    d = {}
    for row in range(height):
        for col in range(width):
            d[(row, col)] = '.'
    return d


rowSize, colSize = 5, 5
grid = makeGrid(rowSize, colSize)

# directions N, NE, E, SE, S, SW, W, NW
dirRow = [-1, -1, 0, 1, 1, 1, 0, -1]
dirCol = [0, 1, 1, 1, 0, -1, -1, -1]


def floodfill(row, col, c1, c2):  # start row, start col, start char, end char
    if row < 0 or row >= rowSize or col < 0 or col >= colSize:  # out of bounds check
        return 0
    if grid[(row, col)] != c1:  # check if current cell is start char
        return 0
    count = 1  # for counting filled cells
    grid[(row, col)] = c2  # fill this cell
    for d in range(8):  # call recursively in every direction
        count += floodfill(row + dirRow[d], col + dirCol[d], c1, c2)
    return count  # total number of filled cells


print(grid)  # initial grid

#    .....
#    .....
#    .....
#    .....
#    .....

print(floodfill(1, 1, '.', 'f'))  # -> 25 cells filled

print(grid)  # filled grid

#    fffff
#    fffff
#    fffff
#    fffff
#    fffff
