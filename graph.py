from collections import deque


def nearest_zombie(grid):
    # create a multi dimensional grid result matching grid
    res = [[0]* len(grid) for _ in range(len(grid[0]))]
    directions = [(1,0), (0,1), (0,-1), (-1,0)]
    
    def dfs_level(pos, level):
        if not pos:
            return
        row,col = pos
        if grid[row][col] == 0:
            return level
        for d in directions:
            r,c = d
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                res = dfs_level((r,c), level + 1)
                if res != 0:
                    return res
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res[i][j] = dfs_level((i,j),0 )
    return res
grid_1 = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]

grid_2 = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
    ]

# print(nearest_zombie(grid_1))
# print(nearest_zombie(grid_2))
def has_path(post,g):
    q = deque()
    q.append(post)
    visited = set()
    while q:
        curr = q.popleft()
        if curr == (2,2):
            return True
        visited.add(curr)
        for c in get_moves(curr,g):
            if c not in visited:
                q.append(c)
    return False


def get_moves(pos, g):
    row,col = pos
    dir = [(1,0) ,(0,1)]
    res = []
    for d in dir:
        r,c = d
        if 0 <= row + r < len(g) and 0 <= col +c < len(g[0]) and  g[row][col] == 1:
            res.append((row+r,col+c))
    return res
def can_disconnect_safehouse(city):
    if has_path((0,2), city):
        print("Can get to end")
    return
city_1 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]

city_2 = [
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 1]
]

print(can_disconnect_safehouse(city_1))  
# print(can_disconnect_safehouse(city_2))  