graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]

n = len(graph)
count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if not(i ==j or i == k or j == k) and graph[i][j] and graph[j][k] and graph[i][k]:
                count += 1

print(count//3)