ans=[]
for i in range(int(input())):
    a,b =  list(int(i)for i in input().split())
    ans.append('0') if b<=a/2 else ans.append('1')
for i in ans:
    print(i)
