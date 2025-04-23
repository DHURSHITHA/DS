class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges):
    mst = []
    disjoint_set = DisjointSet(vertices)
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)
    return mst

def main():
    vertices = input("Enter the cities (separated by spaces): ").split()
    num_edges = int(input("Enter the number of possible connections: "))
    edges = []
    print("Enter each connection in the format: city1 city2 cost")
    for _ in range(num_edges):
        u, v, weight = input().split()
        edges.append((u, v, int(weight)))
    
    mst = kruskal(vertices, edges)
    print("The edges in the Minimum Spanning Tree (MST) are:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")

if __name__ == "__main__":
    main()
Output:
Enter the cities (separated by spaces): A B C D E
Enter the number of possible connections: 7
Enter each connection in the format: city1 city2 cost
A B 1
A C 2
B C 2
B D 5
C D 1
D E 3
C E 6
The edges in the Minimum Spanning Tree (MST) are:
A - B: 1
C - D: 1
A - C: 2
D - E: 3