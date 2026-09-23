# Contribution Log

**Student:** Sanskruti Sandeep Danole  
**PRN:** 25UAM059  
**Division:** A  
**Repository:** AI Workflow Assistant

## Contribution

| Date | Contribution | Tools/Technology | Status |
|---|---|---|---|
| 23 Sep 2026 | Implemented BFS and DFS graph traversal in Python | Python, Data Structures | Completed |
| 23 Sep 2026 | Added execution-time benchmarking | Python `time.perf_counter()` | Completed |
| 23 Sep 2026 | Added performance-profiling instructions | py-spy | Completed |
| 23 Sep 2026 | Added graph/traversal visualization | Mermaid | Completed |
| 23 Sep 2026 | Updated project documentation | Markdown, GitHub | Completed |

## BFS and DFS

The project demonstrates two standard graph traversal algorithms:

- **BFS (Breadth-First Search):** explores nodes level by level using a queue.
- **DFS (Depth-First Search):** explores as deeply as possible before backtracking, using a stack.

Both algorithms search from node **A** to goal node **G**.

## Graph

The example graph is:

```text
        A
       / \
      B   C
     / \ / \
    D  E F  G
```

For the given graph:

- BFS reaches **G** after expanding: A → B → C → D → E → F → G
- DFS reaches **G** after expanding: A → B → D → E → C → F → G

## py-spy Profiling

Install py-spy:

```bash
pip install py-spy
```

Run the program:

```bash
python bfs_dfs.py
```

Record a profiling report:

```bash
py-spy record --output profile.svg -- python bfs_dfs.py
```

The generated `profile.svg` is a flame graph showing where Python spends execution time.

For a live terminal view:

```bash
py-spy top -- python bfs_dfs.py
```

> Note: exact execution-time values depend on the computer and Python environment, so the profiling result should be generated on the machine where the experiment is performed.

## Files

- `bfs_dfs.py` — BFS and DFS implementation with benchmarking.
- `CONTRIBUTION_LOG.md` — contribution record.
- `graph.md` — graph and traversal visualization.

## Conclusion

BFS and DFS provide two different strategies for traversing a graph. The Python implementation measures the number of expanded nodes and execution time, while **py-spy** can be used to inspect the runtime behavior of the program.
