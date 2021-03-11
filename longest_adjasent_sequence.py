def longestAdjacentSequence(matrix):
    rows = len(matrix)
    columns = len(matrix[-1])

    visited = [[False] * rows for i in range(columns)]
    stack = []
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    maxSequenceLen = 0

    for row in range(rows):
        for col in range(columns):
            if visited[row][col]:
                continue
            sequencelen = 0
            stack.append([row, col])
            while stack:
                currentCell = stack.pop()
                currentRow = currentCell[0]
                currentColumn = currentCell[1]

                if (visited[currentRow][currentColumn]):
                    continue
                current = matrix[currentRow][currentColumn]
                visited[currentRow][currentColumn] = True
                sequencelen += 1

                for direction in directions:
                    adjacentRow = currentRow + direction[0];
                    adjacentColumn = currentColumn + direction[1];

                    if adjacentRow < 0 or adjacentRow >= rows  or adjacentColumn < 0 or adjacentColumn >= columns or visited[adjacentRow][adjacentColumn]:
                        continue
                    

                    adjacent = matrix[adjacentRow][adjacentColumn]
                    if current == adjacent:
                        stack.append([adjacentRow, adjacentColumn])

            maxSequenceLen = max(sequencelen, maxSequenceLen)
        return maxSequenceLen


test_1 = [
    [
        'R', 'R', 'B',
    ],
    [
        'G', 'G', 'R',
    ],
    [
        'R', 'B', 'G',
    ]]

test_2 = [
    [
        'R', 'R', 'R', 'G',
    ],
    [
        'G', 'B', 'R', 'G',
    ],
    [
        'R', 'G', 'G', 'G',

    ],
    [
        'G', 'G', 'B', 'B'
    ]]

test_3 = [
    [
        'R', 'R', 'B', 'B', 'B', 'B',
    ],
    [
        'R', 'R', 'B', 'B', 'G', 'B',
    ],
    [
        'B', 'R', 'B', 'B', 'G', 'B',
    ],
    [
        'B', 'B', 'R', 'B', 'G', 'B',
    ],
    [
        'R', 'B', 'R', 'B', 'R', 'B',
    ],
    [
        'R', 'B', 'B', 'B', 'G', 'B',
    ]]
rows = 1000
columns = 1000
test_4 = [[0] * rows] * columns

for row in range(rows):
    for col in range(columns):
        test_4[row][col] = 'R'

print(longestAdjacentSequence(test_1))
print(longestAdjacentSequence(test_2))
print(longestAdjacentSequence(test_3))
print(longestAdjacentSequence(test_4))
