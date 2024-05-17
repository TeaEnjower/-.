things = {}
num = int(input())
for i in range(num):
    itemdata = input('Название вес стоимость ').split()
    things.update({itemdata[0]:(int(itemdata[1]),int(itemdata[2]))})
print(things)
lim=int(input('Емкость сумки '))
def lst_weight_cost(items):
    weight=[items[item][0] for item in items]
    cost=[items[item][1] for item in items]
    return weight, cost
def memoisation(things, lim):
    weight, cost=lst_weight_cost(things)
    n=len(things)
    memtable=[[0 for j in range(lim+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(lim+1):
            if i==0 or j==0:
                memtable[i][j]=0
            elif weight[i-1]<=j:
                memtable[i][j]=max(cost[i-1]+memtable[i-1][j-weight[i-1]],memtable[i-1][j])
            else:
                memtable[i][j]=memtable[i-1][j]
    return memtable, weight, cost
def itemstaken(things,lim):
    memtable, weight, cost=memoisation(things,lim)
    n=len(things)
    res=memtable[n][lim]
    a=lim
    lst_items=[]
    for i in range(n,0,-1):
        if res<=0:
            break
        if res==memtable[i-1][a]:
            continue
        else:
            lst_items.append((weight[i-1],cost[i-1]))
            res-=cost[i-1]
            a-=weight[i-1]
    picked=[]
    for i in lst_items:
        for key,value in things.items():
            if value==i:
                picked.append(key)
    return picked
bag=itemstaken(things,lim)
print(bag)