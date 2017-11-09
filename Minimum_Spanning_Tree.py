def dijkstra(graph,source,stop,visited=[],distance={},previous={}):
    if source==stop:
        path=[]
        pre=stop
        while pre!= None:
            path.append(pre)
            pre=previous.get(pre,None)
            orig=path.reverse()
        print("Shortest Path:" + str(sorted(path)))
        print("Cost:"+str(distance[stop]))
    else:
        if not visited:
           distance[source]=0
        for next_node in graph[source]:
           if next_node not in visited:
               new_distance=distance[source]+graph[source][next_node]
               if new_distance<distance.get(next_node,float('inf')):
                   distance[next_node]=new_distance
                   previous[next_node]=source
        visited.append(source)
        unvisited={}
        for i in graph:
            if i not in visited:
                unvisited[i]=distance.get(i,float('inf'))
        s=min(unvisited,key=unvisited.get)
        dijkstra(graph,s,stop,visited,distance,previous)

G= { 'a' : { 'b' : 5 , 'd' : 7},
     'b' : { 'c' : 6 , 'd' : 8 , 'e' : 7},
     'c' : { 'b' : 6 , 'e' : 9},
     'd' : { 'a' : 7 , 'b' : 8 , 'e' : 8},
     'e' : { 'b' : 7 , 'c' : 9 , 'd' : 8 , 'g' : 9},
     'f' : { 'd' : 8 , 'g' : 5 , 'h' : 7},
     'g' : { 'e' : 9 , 'f' : 5 , 'h' : 9 , 'i' : 8},
     'h' : { 'f' : 7 , 'g' : 9 , 'i' : 11},
     'i' : { 'e' : 15 , 'g' : 8 , 'h' : 11}
    }

s=input("Enter source :")
d=input("Enter destination :")
dijkstra(G,s,d)
