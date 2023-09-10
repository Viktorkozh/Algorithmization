cnt = maxS = 0
file = open('17.txt')
a = [int(i) for i in file]
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i] + a[j]) % 60 == 0 and (a[i] % 40 == 0 or a[j] % 40 == 0):
            cnt += 1
            maxS = max(maxS, a[i] + a[j])
print(cnt, maxS)
