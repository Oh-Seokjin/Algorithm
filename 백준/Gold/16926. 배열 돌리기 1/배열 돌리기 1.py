n, m, r = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(n)]

def move(r):
    global board
    
    for _ in range(r):
        for i in range(min(n, m)//2):
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
    
move(r)

for i in range(n):
    for j in range(m):
        print(board[i][j], end= " ")
    print()