import math

def cal_y(x, r):
    y = (r**2 - x**2)**0.5
    return y

def solution(r1, r2):
    quar = 0
    # 각 사분면
    for x in range(1, r2+1):
        if x < r1:
            s = math.ceil(cal_y(x, r1))
        else:
            s = 0    
        e = math.floor(cal_y(x, r2))
        
        quar += e-s+1
        
    answer = quar * 4
    return answer