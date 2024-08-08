order = 10000
def f():
    with open("big_cycle.txt","w") as file:
        file.write(f"{order}\n") #order of the graph
        file.write(f"1 {order-1}\n") #neighbour of 0
        for i in range(1, order-1):
            file.write(f"{i-1} {i+1}\n")
        file.write(f"0 {order-2}\n") #vertex 99999's neighbours
        file.write("0\n") #finish

f()
