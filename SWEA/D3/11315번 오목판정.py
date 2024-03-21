import sys
sys.stdin = open("input.txt", "r")

di = [0, 1, 1, -1]
dj = [1, 0, 1, 1]

def solve():
    for si in range(N):
        for sj in range(N):
            for dr in range(4):
                for mul in range(5):
                    ni, nj = si + di[dr]*mul, sj + dj[dr]*mul
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == "o":
                        pass
                    else:
                        break
                else:
                    return "YES"
    return "NO"
                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = solve()
    print(f"#{tc} {ans}")