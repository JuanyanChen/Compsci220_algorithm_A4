import sys

input_content = sys.stdin.read().split('\n')
#input_content = open("test.txt","r").read().split('\n')

order_position = 0
order_of_graph = int(input_content[order_position])
graph_number = 0
while order_of_graph != 0:
    result = 0
    print(order_of_graph)
    for i in range(order_position + 1, order_position + order_of_graph + 1):
        out_deg_list = input_content[i].split()
        result_line = ["0"] * order_of_graph
        for j in out_deg_list:
            result_line[int(j)] = "1"
        print(" ".join(result_line))
    order_position += order_of_graph + 1
    order_of_graph = int(input_content[order_position])
print("0")
