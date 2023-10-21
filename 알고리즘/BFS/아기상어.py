from collections import deque

# 고려해야 할 것 : 문제 정리, 분석, 시간복잡도


n = int(input())
space = [list(map(int, input().split())) for i in range(n)]

# 상 우 좌 하
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

loc = []
count = 0
# 초기 상어의 위치
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            loc.append(i)
            loc.append(j)


# 가까운 먹이 탐색 = 최단거리 =bfs
# x,y 는 상어의 현위치
def bfs(x, y):
    ans = []
    visit = [[0] * n for i in range(n)]  # 방문체크
    queue = deque([[x, y]])

    visit[x][y] = 1

    while queue:
        i, j = queue.popleft()

        # 4방향
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]

            # 범위 안에 들고 방문 안한경우
            if 0 <= ni and ni < n and 0 <= nj and nj < n and visit[ni][nj] == 0:
                if space[x][y] > space[ni][nj] and space[ni][nj] != 0:
                    visit[ni][nj] = visit[i][j] + 1
                    ans.append((visit[ni][nj] - 1, ni, nj))
                elif space[x][y] == space[ni][nj]:
                    visit[ni][nj] = visit[i][j] + 1
                    queue.append([ni, nj])
                elif space[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    queue.append([ni, nj])
        return sorted(ans, key = lambda x: (x[0], x[1], x[2]))

i, j = loc
size = [2, 0]

while True:
    space[i][j] = size[0]
    ans = deque(bfs(i, j))

    if not ans:
        break

    step, xx, yy = ans.popleft()
    count += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[i][j] = 0
    i, j = xx, yy

print(count)

# print(loc)
# print(i)
# print(j)
