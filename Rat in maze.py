maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

n = len(maze)

directions = 'UDLR'
i_coords = [-1, 1, 0, 0]
j_coords = [0, 0, -1, 1]

start = (0,0)
end = (n-1,n-1)

curr_path = ''
res = []


def isValid(i,j):
    return 0<=i<n and 0<=j<n and maze[i][j] == 1

def findPath(i,j,curr_path):
    if (i,j) == end:
        res.append(curr_path)
        return
    maze[i][j] = 0

    for k in range(4):
        if isValid(i+i_coords[k],j+j_coords[k]):
            
            curr_path += directions[k]

            findPath(i+i_coords[k],j+j_coords[k],curr_path)

            curr_path = curr_path[:-1]
    maze[i][j] = 1


findPath(0,0,curr_path)


    # Call ratInMaze and get the result
result = res

# Print result in the main function
if not result:
    print(-1)
else:
    print(" ".join(result))