<h1 align="center">Prim’s Algorithm</h1>

## Overview

**Prim’s Algorithm** is a **greedy algorithm** used to find the **Minimum Spanning Tree (MST)** of a **weighted, connected, undirected graph**.

A **Minimum Spanning Tree** is a subset of edges that:

* Connects all vertices in the graph
* Has **no cycles**
* Has the **minimum possible total edge weight**

Prim’s Algorithm starts from any node and gradually expands the tree by adding the **smallest edge that connects a new vertex**.

<a href="/src/main.py">Check out for source code.</a>

---

## 📌 Key Concepts

### Graph

A structure consisting of **vertices (nodes)** connected by **edges**.

### Weighted Graph

Each edge has a **numerical weight or cost**.

### Minimum Spanning Tree (MST)

A tree that connects all vertices with the **minimum total edge weight**.

Example:

If a graph has **V vertices**, the MST will always have:

```
V - 1 edges
```

---

## ⚙️ How Prim’s Algorithm Works

1. Start with any vertex in the graph
2. Add it to the **MST set**
3. Find the **minimum-weight edge** connecting the MST to a new vertex
4. Add that edge and vertex to the MST
5. Repeat until all vertices are included

---

## 🧩 Example Graph

```
       2
   A ------ B
   |        |
  6|        |3
   |        |
   C ------ D
       1
```

### Edge Weights

| Edge | Weight |
| ---- | ------ |
| A–B  | 2      |
| A–C  | 6      |
| B–D  | 3      |
| C–D  | 1      |

---

## 🧪 Step-by-Step Example

Start from **A**

### Step 1

MST = {A}

Possible edges:

```
A–B (2)
A–C (6)
```

Choose **A–B (2)**

---

### Step 2

MST = {A, B}

Possible edges:

```
A–C (6)
B–D (3)
```

Choose **B–D (3)**

---

### Step 3

MST = {A, B, D}

Possible edges:

```
A–C (6)
D–C (1)
```

Choose **D–C (1)**

---

### Final Minimum Spanning Tree

Edges in MST:

```
A – B (2)
B – D (3)
D – C (1)
```

### Total Weight

```
2 + 3 + 1 = 6
```

---

## ⏱️ Time & Space Complexity

| Implementation                        | Time Complexity |
| ------------------------------------- | --------------- |
| Using Adjacency Matrix                | O(V²)           |
| Using Priority Queue + Adjacency List | O(E log V)      |

Where:

* **V** = number of vertices
* **E** = number of edges

**Space Complexity:** O(V)

---

## 🧠 Python Implementation

```python
import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (cost, neighbor))

    return total_cost


graph = {
    'A': [('B',2), ('C',6)],
    'B': [('A',2), ('D',3)],
    'C': [('A',6), ('D',1)],
    'D': [('B',3), ('C',1)]
}

print(prim(graph,'A'))
```

### Output

```
6
```

---

## 👍 Advantages

* Efficient for **dense graphs**
* Guarantees the **minimum spanning tree**
* Easy to implement with priority queues

---

## 👎 Disadvantages

* Only works on **connected graphs**
* Requires extra memory for storing the graph
* Less efficient for very sparse graphs compared to other methods

---

## 📊 Prim’s vs Kruskal’s Algorithm

| Feature        | Prim’s Algorithm      | Kruskal’s Algorithm        |
| -------------- | --------------------- | -------------------------- |
| Strategy       | Greedy (vertex-based) | Greedy (edge-based)        |
| Start          | Begins from a vertex  | Begins with smallest edges |
| Best for       | Dense graphs          | Sparse graphs              |
| Data structure | Priority Queue        | Union-Find                 |

---

## 📌 When to Use Prim’s Algorithm

Use Prim’s Algorithm when:

* You need a **Minimum Spanning Tree**
* The graph is **connected and weighted**
* The graph is **dense (many edges)**

Common applications include:

* Network design
* Road and railway construction
* Electrical grid design
* Telecommunications networks

---

## 🏁 Summary

Prim’s Algorithm is an efficient greedy algorithm for constructing a **Minimum Spanning Tree** in a weighted graph. By always choosing the smallest connecting edge, it ensures that the resulting tree has the minimum possible total weight.
