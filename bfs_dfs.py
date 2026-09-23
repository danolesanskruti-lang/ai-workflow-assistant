from collections import deque
import time

# Graph used for BFS and DFS
GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}


def bfs(start, goal):
    """Breadth-First Search using a queue."""
    queue = deque([start])
    visited = {start}
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in GRAPH[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return nodes_expanded


def dfs(start, goal):
    """Depth-First Search using a stack."""
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

        for neighbour in reversed(GRAPH[node]):
            stack.append(neighbour)

    return nodes_expanded


def benchmark(search_function, start="A", goal="G"):
    """Measure execution time and nodes expanded."""
    start_time = time.perf_counter()
    nodes = search_function(start, goal)
    end_time = time.perf_counter()

    time_taken_ms = (end_time - start_time) * 1000
    return nodes, time_taken_ms


if __name__ == "__main__":
    bfs_nodes, bfs_time = benchmark(bfs)
    dfs_nodes, dfs_time = benchmark(dfs)

    print("----- BFS -----")
    print("Nodes Expanded:", bfs_nodes)
    print("Execution Time: {:.6f} ms".format(bfs_time))

    print("\n----- DFS -----")
    print("Nodes Expanded:", dfs_nodes)
    print("Execution Time: {:.6f} ms".format(dfs_time))
