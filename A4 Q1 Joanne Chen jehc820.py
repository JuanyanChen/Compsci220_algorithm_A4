import sys

input_content = sys.stdin.read().split('\n')

order_position = 0
order_of_graph = int(input_content[order_position])
graph_number = 0
while order_of_graph != 0:
    result = 0
    graph_number += 1
    for i in range(order_position + 1, order_position + order_of_graph + 1):
        result += len(input_content[i].split())           
    order_position += order_of_graph + 1
    order_of_graph = int(input_content[order_position])
    print("Graph {} has size {}.".format(graph_number, int(result/2)))

