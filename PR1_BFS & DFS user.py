# BFS CODE
def bfs(graph, start):
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# DFS CODE
def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# Initialize an empty graph
graph = {}

# Input the graph nodes and edges interactively
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter the name of node {i + 1}: ")
    neighbors = input(f"Enter neighbors of {node} (comma-separated): ").split(',')
    graph[node] = [n.strip() for n in neighbors]

start_node = input("Enter the starting node: ")

print("Breadth-First Search (BFS):")
bfs(graph, start_node)
print("\n")

print("Depth-First Search (DFS):")
visited = set()
dfs(graph, start_node, visited)


"""Output:
Enter the number of nodes: 6
Enter the name of node 1: A
Enter neighbors of A (comma-separated): B, C
Enter the name of node 2: B
Enter neighbors of B (comma-separated): D, E
Enter the name of node 3: C
Enter neighbors of C (comma-separated): F
Enter the name of node 4: D
Enter neighbors of D (comma-separated): 
Enter the name of node 5: E
Enter neighbors of E (comma-separated): F
Enter the name of node 6: F
Enter neighbors of F (comma-separated): 

Enter the starting node: A

Breadth-First Search (BFS):
A B C D E F 

Depth-First Search (DFS):
A
B
D
E
F
C
"""