import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    M = N//2
    s, e = M, M
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]
        if i < M:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f"#{tc} {ans}")