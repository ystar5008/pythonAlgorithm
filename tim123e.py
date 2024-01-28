import random

findNumber = random.randrange(1, 101)

for i in range(1, 101):
    if i == findNumber:
        print(i)
        break


N = 100000
cnt = 1

for i in range(N):
    print(str(cnt))
    cnt += 1
