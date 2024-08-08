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

def traverse(visited, q, adjacency_list, node):
    if len(adjacency_list[node]) == 0: #disconnected if no neighbour for this node       
        return 1
    else:
        component_order = 0
        if visited[int(node)] != "1":
            visited[int(node)] = "1" #turn visited node to "1" means it has been visited
            q.append(str(node)) #append nodes not visited            
        while len(q) != 0: #when q is not empty, visit every node in q
            temp_node = q.popleft() #returns the first element and removes it
            component_order += 1
            for connected_node in adjacency_list[int(temp_node)]:
                if visited[int(connected_node)] != "1":
                    q.append(connected_node)
                    visited[int(connected_node)] = "1"
                          
        return component_order
        
while order_of_graph != 0:
    largest_order = 0    
    adjacency_list = create_adjacency_list(order_of_graph)
    visited = ["0"] * order_of_graph # Hash table for visited node
    q = collections.deque() #Initialize a queue for non-travesed nodes

    for i in range(order_of_graph):        
        if order_of_graph == len(adjacency_list[i]) + 1: #if a node connects all other nodes
            largest_order = order_of_graph
            break
        else:
            component_order = traverse(visited, q, adjacency_list, i)
            if component_order > largest_order: largest_order = component_order #update result if new order is larger
            
    #print(adjacency_list) #for test
    order_position += order_of_graph + 1
    order_of_graph = int(input_content[order_position])
    graph_number += 1
    print("Graph {} has a component of order {}.".format(graph_number, largest_order))
                            
#print(time.time()-start) #for test
