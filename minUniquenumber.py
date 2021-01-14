ans = []
for i in range(int(input())):
    p = int(input())
    x = list(map(int,input().split()[:p]))
    y = list(filter(lambda v: x.count(v)==1,x))
    m = x.index(min(y))+1 if len(y)!=0 else -1
    ans.append(m)
for i in ans:
    print(i)