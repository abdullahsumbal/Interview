grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
maxIncrease = 0
# if(not len(grid)):
#     return maxIncrease
rowLen = len(grid)
colLen = len(grid[0])

maxRowList = []
maxColList = []

maxRow = 0
maxCol = 0

for row in grid:
    maxRowList.append(max(row))


for j in range(colLen):
    for i in range(rowLen):
        if(maxCol < grid[i][j]):
            maxCol = grid[i][j]
    maxColList.append(maxCol)
    maxCol = 0

print(maxColList)
print(maxRowList)
for i in range(rowLen):
    for j in range(colLen):
        diff = min(maxColList[j], maxRowList[i]) - grid[i][j]
        if(diff > 0):
            maxIncrease += diff

print(maxIncrease)
