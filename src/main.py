import heapq  # Used for the priority queue (min-heap) to efficiently find the minimum weight edge
import sys    # Used to represent infinity for initial distances

class Graph:
    """
    A class to represent a weighted undirected graph using an adjacency list.
    """
    def __init__(self, vertices):
        # Store the number of vertices in the graph
        self.V = vertices
        # Initialize the adjacency list: a dictionary where keys are node IDs 
        # and values are lists of (neighbor, weight) tuples.
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        """
        Adds a weighted undirected edge between vertex u and vertex v.
        """
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def prim_mst(self, start_node=0):
        """
        Implements Prim's Algorithm to find the Minimum Spanning Tree (MST).
        
        Returns:
            mst_edges: A list of edges (u, v, weight) that form the MST.
            total_weight: The sum of weights of the MST edges.
        """
        # 1. INITIALIZATION
        # min_heap stores tuples of (edge_weight, current_node, parent_node)
        # We start with the start_node, weight 0, and no parent (-1).
        min_heap = [(0, start_node, -1)]
        
        # visited keeps track of nodes already included in the MST
        visited = [False] * self.V
        
        # mst_edges stores the final resulting edges of the MST
        mst_edges = []
        total_weight = 0

        print(f"\n--- Starting Prim's Algorithm from Node {start_node} ---")
        print(f"{'Step':<5} | {'Edge Added':<15} | {'Weight':<10} | {'MST Current Weight'}")
        print("-" * 55)

        step = 1
        # 2. MAIN LOOP
        # Continue until the heap is empty (or we've visited all reachable nodes)
        while min_heap:
            # Extract the edge with the smallest weight connecting a node in MST to one outside
            weight, u, parent = heapq.heappop(min_heap)

            # If the node 'u' is already in the MST, skip it
            if visited[u]:
                continue

            # Mark node 'u' as visited (added to MST)
            visited[u] = True
            total_weight += weight
            
            # If it's not the very first node, record the edge
            if parent != -1:
                mst_edges.append((parent, u, weight))
                print(f"{step:<5} | {parent} -- {u:<10} | {weight:<10} | {total_weight}")
                step += 1

            # 3. RELAXATION / EXPLORATION
            # Look at all neighbors of the newly added node 'u'
            for v, edge_weight in self.adj[u]:
                # If the neighbor 'v' is not yet in the MST, add the edge to the heap
                if not visited[v]:
                    heapq.heappush(min_heap, (edge_weight, v, u))

        return mst_edges, total_weight

def visualize_graph_structure():
    """
    A simple text-based illustration of how the algorithm views a graph.
    """
    illustration = """
    ILLUSTRATION OF THE PROCESS:
    Imagine a graph like a set of islands (nodes) and bridges (weighted edges).
    
    1. Start at any island (e.g., Node 0).
    2. Look at all bridges connecting your current islands to new ones.
    3. Pick the CHEAPEST bridge and cross it.
    4. Now you own both islands. Repeat step 2, looking at ALL bridges 
       connected to ANY island you own.
    
    Example Graph Representation:
          (2)       (3)
       0-------1---------2
       |     / |       / |
    (6)|  (8)  |(5) (7)  |(1)
       | /     |   /     |
       3-------4---------5
          (9)       (4)
    """
    print(illustration)

def run_examples():
    # --- EXAMPLE 1: Standard Graph ---
    print("\n" + "="*50)
    print("EXAMPLE 1: Standard Undirected Weighted Graph")
    g1 = Graph(6)
    g1.add_edge(0, 1, 2)
    g1.add_edge(0, 3, 6)
    g1.add_edge(1, 2, 3)
    g1.add_edge(1, 3, 8)
    g1.add_edge(1, 4, 5)
    g1.add_edge(2, 4, 7)
    g1.add_edge(2, 5, 1)
    g1.add_edge(3, 4, 9)
    g1.add_edge(4, 5, 4)

    edges, total = g1.prim_mst(0)
    print(f"\nFinal MST Weight: {total}")
    print(f"Edges in MST: {edges}")

    # --- EXAMPLE 2: A Smaller, Dense Graph ---
    print("\n" + "="*50)
    print("EXAMPLE 2: Small Dense Triangle")
    g2 = Graph(3)
    g2.add_edge(0, 1, 10)
    g2.add_edge(1, 2, 20)
    g2.add_edge(0, 2, 5) # This should be picked over the 10-20 path
    
    edges2, total2 = g2.prim_mst(0)
    print(f"\nFinal MST Weight: {total2}")
    print(f"Edges in MST: {edges2}")

if __name__ == "__main__":
    # Display the visual guide first
    visualize_graph_structure()
    
    # Run the programmed examples
    run_examples()
    
    print("\n" + "="*50)
    print("ALGORITHM SUMMARY:")
    print("1. Time Complexity: O(E log V) using a Binary Heap.")
    print("2. Space Complexity: O(V + E) for the adjacency list and heap.")
    print("3. Prim's is a 'Greedy' algorithm; it always makes the locally optimal choice.")