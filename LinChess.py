ans = []
for i in range(int(input())):
    maxv = 1000000000
    val = -1
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()[:n]))
    for j in a:
        if k%j==0 and k/j<maxv:
            maxv=k/j
            val = j
    ans.append(val)
for i in ans:
    print(i)