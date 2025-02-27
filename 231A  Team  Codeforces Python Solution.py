n = int(input())
accepted = 0

for i in range(n):
    lst = list(map(int, input().strip().split()))
    total = lst[0] + lst[1] + lst[2]
    if total >= 2:
        accepted += 1
print(accepted)