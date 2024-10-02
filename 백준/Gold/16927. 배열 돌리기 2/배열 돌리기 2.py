n, m, r = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(n)]
cycle = 2*(n-1) + 2*(m-1)

def move(r):
    global board
    global cycle
    
    for i in range(min(n, m)//2):
        for _ in range(r%cycle):
            s_x, s_y = i, i
            temp = board[s_x][s_y]
            
            # 좌
            for j in range(i+1, n-i):
                s_x = j
                prev_value = board[s_x][s_y]
                board[s_x][s_y] = temp
                temp = prev_value
            
            # 하
            for j in range(i+1, m-i):
                s_y = j
                prev_value = board[s_x][s_y]
                board[s_x][s_y] = temp
                temp = prev_value
                            
            # 우
            for j in range(i+1, n-i):
                s_x = n - j - 1
                prev_value = board[s_x][s_y]
                board[s_x][s_y] = temp
                temp = prev_value            
            
            # 상
            for j in range(i+1, m-i):
                s_y = m - j - 1
                prev_value = board[s_x][s_y]
                board[s_x][s_y] = temp
                temp = prev_value
        cycle -= 8
    
move(r)

for i in range(n):
    for j in range(m):
        print(board[i][j], end= " ")
    print()