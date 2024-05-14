with open('test.format1.txt') as f:
    n = int(f.readline())
    a = [tuple(map(int, i.split())) for i in f.readlines()]

a_set = set(a)
neighbors = set()
neighbors.add(a[0])

poss = {}

for i in a:
    poss[i] = []
    a, b = i
    if (a+1, b) in a_set:
        poss[i].append((a+1, b, 'R'))
    if (a, b+1) in a_set:
        poss[i].append((a, b+1, 'T'))
    if (a-1, b) in a_set:
        poss[i].append((a-1, b, 'L'))
    if (a, b-1) in a_set:
        poss[i].append((a, b-1, 'B'))


def res(graph, s):
    neigh = set()
    neigh.add(s)
    queue = [s]
    ans = []
    ans.append(' '.join(list(map(str, s))))          
    while queue:                         
        v = queue.pop(0)
        c_2 = 0
        ans_cur = ''          
        for w in graph[v[:2]]:
            if w[:2] not in neigh:           
                queue.append(w)
                ans_cur += w[2]
                neigh.add(w[:2])
                c_2 += 1
        if c_2 == 0:
            ans.append("")
        else:
            ans.append(ans_cur)

    return ans

n = res(poss, (2, 3))

with open('test.format2.txt', 'w') as f:
    ans = ',\n'.join(n)
    f.write(ans)
    f.write('.')
