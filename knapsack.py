def retailer():
    poss,i,check,f_weight,weigh,cost_t=[],0,0,[],[],[]
    w,n=list(map(int,input("Enter total weight and number of retailers\n").split()))
    weight,cost=list(map(int,input("\nEnter weights of retailers\n").split()[:n])),list(map(int,input("\nEnter cost of retailers\n").split()[:n]))
    while(len(weight)>i):
        if(weight[i]<=w): poss.append(weight[i]) 
        else:
            weight.pop(i)
            cost.pop(i)
        i+=1
    if(len(poss)==0): 
        print("no possibility")
        return False
    elif(len(poss)==1): 
        print(cost)
        return False
    for i in poss: check=check+i
    if(check<w): 
        check=0
        for z in cost: check=check+z
        print("\n\nans ==== ",check)  
        return False
    lists,check = [[]],0 
    for i in range(len(poss)):
        orig = lists[:] 
        new = poss[i] 
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
            total=0 
            for i in lists[j]: 
                if((total+i)<w): total=total+i
        lists = orig + lists 
    for i in range(len(lists)):
        check=0
        for z in range(len(lists[i])): check=check+lists[i][z]
        if(check<=w):
            weigh.append(check)
            f_weight.append(lists[i])
    for i in range(len(f_weight)):
        totall=0
        for z in f_weight[i]:
            red=weight.index(z)
            totall=totall+cost[red]
        cost_t.append(totall)
    print("\nans =========",max(cost_t))
retailer()