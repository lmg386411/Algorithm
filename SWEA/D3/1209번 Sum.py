import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    _ = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    mx = 0
    sm_a = 0
    sm_b = 0
    for i in range(100):
        sm_x = 0
        sm_y = 0
        for j in range(100):
            sm_x += arr[i][j]
            sm_y += arr[j][i]
        if mx < sm_x:
            mx = sm_x
        if mx < sm_y:
            mx = sm_y
        sm_a += arr[i][i]
        sm_b += arr[i][99-i]
    if mx < sm_a:
        mx = sm_a
    if mx < sm_b:
        mx = sm_b
    print(f"#{tc} {mx}")