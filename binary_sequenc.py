n=int(input())
a = []
for i in range(2**n):
  s = bin(i)[2:]
  if len(s)>n:
    s = s[::-1]
    s = s[:n]
  if len(s)<n:
    s = '0'*(n-len(s))+s
  a.append(s)
print(a)