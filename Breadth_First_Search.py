G={1: set([2,8,11]),
   2: set([1,3,4,7]),
   3: set([2]),
   4: set([2,5,6]),
   5: set([4]),
   6: set([4]),
   7: set([2]),
   8: set([1,9,10]),
   9: set([8]),
   10: set([8]),
   11: set([1,12,13,16]),
   12: set([11]),
   13: set([11,14,15]),
   14: set([13]),
   15: set([13]),
   16: set([11])}

def enumerate_path(graph,begin,stop):
    queue= [(begin,[begin])]
    while queue:
        (vertex,path)=queue.pop(0)
        for next in (graph[vertex]-set(path)):
            if(next==stop):
                yield path+[next]
            else:
                queue.append((next,path+[next]))

def short(graph,begin,stop):
    try:
        print(next(enumerate_path(graph,begin,stop)))
    except:
        None

source=int(input("Enter source: "))

for i in range(1,13,1):
    short(G,source,i)


