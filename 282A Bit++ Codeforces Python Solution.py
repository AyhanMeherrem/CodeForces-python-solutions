n = int(input())
value = 0
for i in range(n):
    line = input()
    if line[1]+line[2]=="++" or line[1]+line[0]== "++":
        value += 1
    elif line[1]+line[2]=="--" or line[1]+line[0]== "--":
        value -=1
print(value)