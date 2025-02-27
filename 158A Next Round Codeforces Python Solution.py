lst = list(map(int, input().rstrip().split()))
scores = list(map(int, input().rstrip().split()))
k = lst[1]
threshold = scores[k-1]
passed = sum(1 for score in scores if score >= threshold and score > 0)
print(passed)