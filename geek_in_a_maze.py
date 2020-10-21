"""Geek is in a maze of size N * M.
Each cell in the maze is made of either '.' or '#'.
An empty cell is represented by '.' and an obstacle is represented by '#'.
If Geek starts at cell (R, C), find how many different empty cells he can pass through while avoiding the obstacles.
He can move in any of the four directions but he can move up at most U times and he can move down atmost D times.
"""

import heapq as hq


def isValid(row, col, n, m):
    if 0 <= row < n and 0 <= col < m:
        return True


def numberOfCells(n, m, r, c, u, d, mat):
    pque = []
    vis = [[0 for i in range(m)] for j in range(n)]

    hq.heappush(pque, ((0, 0), (r, c)))
    vis[r][c] = 1

    while pque:
        up, down = pque[0][0][0], pque[0][0][1]

        x, y = pque[0][1][0], pque[0][1][1]

        hq.heappop(pque)

        if isValid(x - 1, y, n, m):
            if up + 1 <= u and not vis[x - 1][y] and down <= d and mat[x - 1][y] == '.':
                hq.heappush(pque, (((up + 1), down), (x - 1, y)))
                vis[x - 1][y] = 1

        if isValid(x + 1, y, n, m):

            if down + 1 <= d and not vis[x + 1][y] and up <= u and mat[x + 1][y] == '.':
                hq.heappush(pque, ((up, (down + 1)), (x + 1, y)))
                vis[x + 1][y] = 1

        if isValid(x, y - 1, n, m):
            if down <= d and not vis[x][y - 1] and up <= u and mat[x][y - 1] == '.':
                hq.heappush(pque, ((up, down), (x, y - 1)))
                vis[x][y - 1] = 1

        if isValid(x, y + 1, n, m):
            if down <= d and not vis[x][y + 1] and up <= u and mat[x][y + 1] == '.':
                hq.heappush(pque, ((up, down), (x, y + 1)))
                vis[x][y + 1] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 1:
                ans += 1

    return ans

if __name__ == '__main__':
    t = int(int(input()))

    for tcs in range(t):
        n,m,r,c,u,d = [int(x) for x in input().split()]

        mat = []

        for i in range(n):
            matele = [x for x in input()]
            mat.append(matele)

        print(numberOfCells(n, m, r, c, u, d, mat))

# Give input as
# 1
# 3 3 1 0 1 1
# ...
# .#.
# #..
