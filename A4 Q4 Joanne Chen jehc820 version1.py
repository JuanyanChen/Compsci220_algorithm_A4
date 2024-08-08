import sys
import time
import collections

#input_content = sys.stdin.read().split('\n')
input_content = open("unstop.txt","r").read().split('\n')

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

def dijkstra(a_graph, node):
    visited = [0] * order_of_graph #hash table    
    visited[node] = 1    
    max_distance = 0

    distance = [float("inf")] * order_of_graph #distance list
    distance[node] = 0 #distance from node to itself is zero
    for neighbour in a_graph[node]:
        distance[int(neighbour)] = 1 #neighbour has finit distance 1, other nodes has infinite distance
    #print(distance) #test
            
    while 0 in visited:
        big = float("inf")
        for vertex in range(len(a_graph)): #find unvisited node u with dist[u] is minimum
            if visited[int(vertex)] == 0:               
                if distance[int(vertex)] < big:
                    u = vertex
                    big = distance[int(vertex)]
                    
        visited[u] = 1
        for x in a_graph[u]: #x is neighbour of u
            x = int(x)
            if visited[x] == 0:
                distance[x] = min(distance[x], distance[u] + 1) #x is u's neighbour in unweighted graph, so c[u,x] == 1
            print(distance) #test
        d = max(distance)
    if d > max_distance: max_distance = d
    return max_distance
        
while order_of_graph != 0:
    result = 0
    graph_number += 1
    diameter = 0
    a_graph = create_adjacency_list(order_of_graph)
    #if graph_number == 137: print(a_graph)
    #print(a_graph)

    for node in range(order_of_graph):
        if [] in a_graph:
            diameter = float("inf")
            break
        else:
            max_distance = dijkstra(a_graph, node) #the max distance from starting node to each node         
            if diameter < max_distance:              
                diameter = max_distance
            #print(diameter)
            
    if diameter == float("inf"):
        print("Graph {} is disconnected.".format(graph_number))        
    else:
        print("Graph {} has diameter {}.".format(graph_number, diameter))
    
    order_position += order_of_graph + 1
    order_of_graph = int(input_content[order_position])
