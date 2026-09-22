import time

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            stack.append(neighbour)

    return nodes_expanded


start_time = time.perf_counter()

nodes = dfs('A', 'G')

end_time = time.perf_counter()

time_taken = (end_time - start_time) * 1000

print("----- DFS -----")
print("Nodes Expanded:", nodes)
print("Execution Time:", time_taken, "ms")