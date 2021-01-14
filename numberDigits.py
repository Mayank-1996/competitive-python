from math import ceil
res = lambda x : ceil(x/9)
times = int(input())
ans=[]
for i in range(times):
    a,b = input().split()
    ans.append(('0',res(int(a)))) if res(int(a))<res(int(b)) else ans.append(('1',res(int(b))))
for i,j in ans:
    print(i,j)