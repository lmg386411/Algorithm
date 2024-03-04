import sys
sys.stdin = open("input.txt", "r")

nums = [2, 3, 5, 7, 11]
T = int(input())
for tc in range(1, T+1):
    cnts = [0] * 5
    N = int(input())
    for i in range(5):
        while N % nums[i] == 0:
            N /= nums[i]
            cnts[i] += 1
    print(f"#{tc}", *cnts)