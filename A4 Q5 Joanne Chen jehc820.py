import sys
import time
import collections

#start = time.time() #for test

input_content = sys.stdin.read().split('\n')
#input_content = open("test.txt","r").read().split('\n') #for test

order_position = 0
order_of_graph = int(input_content[order_position])
graph_number = 0

def create_adjacency_list(order_of_graph): 
    adjacency_list = []
    for i in range(order_of_graph): adjacency_list.append([])
    for i in range(order_of_graph):
        out_deg_list = input_content[order_position + 1 + i].split()
        adjacency_list[i]= out_deg_list
    return adjacency_list

def bfs(adjacency_list,node):
    distance = [0] * len(adjacency_list) #track each vertex from starting vertex
    distance[node] = 0
    q.append(node) #append nodes not visited
    visited[node] = 1
    cycle_length = float("inf")
    if len(adjacency_list[node]) == 0: return float("inf")
    while len(q) != 0: #when q is not empty, visit every node in q        
        curr = q.popleft() #returns the first element and removes it
        for neighbour in adjacency_list[curr]:
            neighbour = int(neighbour)
            if visited[neighbour] != 1:
                visited[neighbour] = 1
                pred[neighbour] =  curr #curr is pred of neighbour
                q.append(neighbour)                
                distance[neighbour] = distance[int(curr)] + 1
                #print(f"distance from {neighbour} to start:", distance[neighbour]) #for test
            elif (visited[neighbour] == 1) and (neighbour != pred[curr]): #a cycle found
                #print(f"neighbour, curr:", neighbour,curr) #for test
                d = distance[int(neighbour)] + distance[int(curr)] + 1
                if d == 3: return d
                elif cycle_length > d: cycle_length = d
                
    return cycle_length
                
while order_of_graph != 0:
    pred = [0] * order_of_graph #for tracking parent node of each node
    q = collections.deque() #Initialize a queue for non-travesed nodes
    girth = float("inf")
    adjacency_list = create_adjacency_list(order_of_graph)
    
    
    for node in range(order_of_graph):
        visited = [0] * order_of_graph # Hash table for visited node
        cycle_length = bfs(adjacency_list,node)
        #print("cycle_length", cycle_length) #for test
        if cycle_length == 3:
            girth = 3 #3 is the smallest cycle, if encounter 3 then stop loop immediately
            break
        elif cycle_length == order_of_graph:
            girth = cycle_length
            break
        elif cycle_length < girth: girth = cycle_length 
    
    order_position += order_of_graph + 1
    order_of_graph = int(input_content[order_position])
    graph_number += 1
    if girth != float("inf") :
        print("Graph {} has girth {}.".format(graph_number, girth))
    else:
        print("Graph {} has girth infinity.".format(graph_number))
                                
#print(time.time()-start) #for test
