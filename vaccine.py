inp = list(map(int,input().split()))
inp_dict = {inp[0]:inp[1],inp[2]:inp[3]}
s = inp[0] if inp[0]<inp[2] else inp[2]
vc,dy = 0,s-1
for i in range(abs(inp[0]-inp[2])):
    if vc>=inp[4]:
        break
    vc += inp_dict[s]
    dy+=1
while vc<inp[4]:
    vc+= (inp_dict[inp[0]]+inp_dict[inp[2]])
    dy+=1
print(dy)   