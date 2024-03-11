import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for _ in range(N):
        lst.sort()
        lst[0] += 1
        lst[-1] -= 1
    print(f"#{tc} {max(lst) - min(lst)}")