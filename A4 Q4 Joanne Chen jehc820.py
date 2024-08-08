import sys
import time
import collections

#input_content = sys.stdin.read().split('\n')
input_content = open("short_test.txt","r").read().split('\n')

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

def dijkstra(a_graph, s):
    q = collections.deque() #priority queue
    colour = ["w"] * order_of_graph #hash table    
    colour[s] = "g"
    tup = (s, 0) #key = 0
    q.append(tup)

    distance = [float("inf")] * order_of_graph
    distance[node] = 0 #distance from node to itself is zero
    for neighbour in a_graph[node]:
        distance[int(neighbour)] = 1 #neighbour has finit distance 1, other nodes has infinite distance
    print(distance) #test
            
    while q:
        u, distance[u] = q.popleft()
        for x in a_graph[u]:
            x = int(x)
            t = distance[u] +1
            if colour[x] == "w":
                colour[x] = "g"
                a_tup = (x,t)
                q.append(a_tup)
            elif colour[x] = "g" and 
    return max_distance
        
while order_of_graph != 0:
    result = 0
    graph_number += 1
    diameter = 0
    a_graph = create_adjacency_list(order_of_graph)
    #print(a_graph) #for test

    for s in range(order_of_graph):
        if len(a_graph[node]) == 0:
            diameter = float("inf")
            break
        else:
            max_distance = dijkstra(a_graph, s) #the max distance from starting node to each node
            print(max_distance) #test
            if diameter < max_distance:
                #print(diameter)
                diameter = max_distance
    
    if diameter == float("inf"):
        print("Graph {} is disconnected.".format(graph_number))        
    else:
        print("Graph {} has diameter {}.".format(graph_number, diameter))
    
    order_position += order_of_graph + 1
    order_of_graph = int(input_content[order_position])
