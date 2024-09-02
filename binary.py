graph = {}
def add_node(graph,node):
    if node not in graph:
        graph[node] = {}

def add_edges(graph,node,edges):
    if node in graph:
        for edge, cost in edges.items():
            if edge in graph:
                graph[node][edge] = cost
            else:
                print(f'Node{edge} does not exist in the graph!')
    else:
        print(f'Node {node} does not exist in the graph')
def delete_edges(graph,node,edges):
    if node in graph:
        for edge in edges:
            if edge in graph[node]:
                del graph[node][edge]
            else:
                print(f'Node {edge} does not exist in node{node}')
    else:
        print(f'Node {node} does not exit in the graph!')
add_node(graph,'A')
add_node(graph,'B')
add_node(graph,'E')
add_node(graph,'C')
add_edges(graph,'A',{'B': 1,'C' : 4})
add_edges(graph,'B',{'A': 1,'C': 5})
add_edges(graph,'C',{'E':1})
add_edges(graph,'E',{'A':4,'E':0})
print(graph)
delete_edges(graph,'A',['E'])
print(graph)
def get_cheapest_node(costs_dict,processed_list):
    cheapest_cost = float('inf')
    cheapest_key = None
    for name,cost in costs_dict.items():
        if name not in processed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_key = name

    return cheapest_key

costs = {}
parents = {}
for name in graph.keys():
    costs[name] = float('inf')
processed = []
current_node ='A'
costs[current_node] = 0
parents[current_node] = None
while current_node:
    for neighbour in graph[current_node]:
        if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
            costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node

    processed.append(current_node)
    current_node = get_cheapest_node(costs,processed)

for d,c in costs.items():
    print(f'The cost for {d} is {c}')