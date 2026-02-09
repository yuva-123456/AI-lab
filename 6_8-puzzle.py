from collections import deque

goal = [[1,2,3],[4,5,6],[7,8,0]]
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def show(s):
    for r in s: print(r)
    print()

def bfs(start):
    q = deque([(start, [])])
    seen = {tuple(map(tuple, start))}
    while q:
        s, path = q.popleft()
        if s == goal:
            return path + [s]
        for i in range(3):
            for j in range(3):
                if s[i][j] == 0: x, y = i, j
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                ns = [r[:] for r in s]
                ns[x][y], ns[nx][ny] = ns[nx][ny], ns[x][y]
                t = tuple(map(tuple, ns))
                if t not in seen:
                    seen.add(t)
                    q.append((ns, path + [s]))

start = [[1,2,3],[4,0,6],[7,5,8]]
for state in bfs(start):
    show(state)
