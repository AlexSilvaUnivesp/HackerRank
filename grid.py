def grid_challenge(grid):
    l = len(grid)
    s = len(grid[0])
    for i in range(l):
        grid[i] = sorted(grid[i])
    for i in range(l-1):
        for j in range(s):
            if ord(grid[i][j]) > ord(grid[i+1][j]): return 'NO' 
    return 'YES'


grid = ['mpxz', 'abcd', 'wlmf']

print(grid_challenge(grid))