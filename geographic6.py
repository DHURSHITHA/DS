import numpy as np

class QuadTreeNode:
    def __init__(self, boundary):
        self.boundary = boundary
        self.cities = []
        self.children = [None, None, None, None]

class QuadTree:
    def __init__(self, boundary, capacity):
        self.root = QuadTreeNode(boundary)
        self.capacity = capacity

    def insert(self, city):
        self._insert_recursive(self.root, city)

    def _insert_recursive(self, node, city):
        if len(node.cities) < self.capacity:
            node.cities.append(city)
        else:
            if node.children[0] is None:
                self._subdivide(node)
            for i in range(4):
                if self._contains(node.children[i].boundary, city):
                    self._insert_recursive(node.children[i], city)

    def _subdivide(self, node):
        x, y, w, h = node.boundary
        half_w = w / 2
        half_h = h / 2
        node.children[0] = QuadTreeNode((x + half_w, y, half_w, half_h))
        node.children[1] = QuadTreeNode((x, y, half_w, half_h))
        node.children[2] = QuadTreeNode((x, y + half_h, half_w, half_h))
        node.children[3] = QuadTreeNode((x + half_w, y + half_h, half_w, half_h))
        for city in node.cities:
            for i in range(4):
                if self._contains(node.children[i].boundary, city):
                    self._insert_recursive(node.children[i], city)
        node.cities = []

    def _contains(self, boundary, city):
        x, y, w, h = boundary
        return x <= city[0] < x + w and y <= city[1] < y + h

    def query_location(self, query_point):
        return self._query_location_recursive(self.root, query_point)

    def _query_location_recursive(self, node, query_point):
        if node is None:
            return []
        if not self._contains(node.boundary, query_point):
            return []
        if node.children[0] is None:
            return node.cities
        result = []
        for i in range(4):
            result.extend(self._query_location_recursive(node.children[i], query_point))
        return result

    def query_nearest_city(self, query_point):
        return self._query_nearest_city_recursive(self.root, query_point, float('inf'), None)

    def _query_nearest_city_recursive(self, node, query_point, min_dist, nearest_city):
        if node is None:
            return nearest_city
        if not self._contains(node.boundary, query_point):
            return nearest_city
        for city in node.cities:
            dist = np.linalg.norm(np.array(city) - np.array(query_point))
            if dist < min_dist:
                min_dist = dist
                nearest_city = city
        if node.children[0] is not None:
            for i in range(4):
                nearest_city = self._query_nearest_city_recursive(
                    node.children[i], query_point, min_dist, nearest_city)
        return nearest_city

# User Input
boundary = tuple(map(int, input("Enter the map boundary (x, y, width, height): ").split()))
capacity = int(input("Enter the capacity of each quadtree node: "))
quadtree = QuadTree(boundary, capacity)

# Insert cities into the quadtree
num_cities = int(input("Enter the number of cities to insert: "))
cities = []
for _ in range(num_cities):
    city = tuple(map(int, input("Enter city coordinates (x, y): ").split()))
    cities.append(city)
    quadtree.insert(city)

# Query for city locations and nearest city
query_point = tuple(map(int, input("Enter the query point (x, y): ").split()))
print("Cities near query point:", quadtree.query_location(query_point))
nearest_city = quadtree.query_nearest_city(query_point)
print("Nearest city to query point:", nearest_city)
Output:
Enter the map boundary (x, y, width, height): 0 0 100 100
Enter the capacity of each quadtree node: 4
Enter the number of cities to insert: 5
Enter city coordinates (x, y): 20 30
Enter city coordinates (x, y): 50 70
Enter city coordinates (x, y): 80 50
Enter city coordinates (x, y): 10 90
Enter city coordinates (x, y): 40 10
Enter the query point (x, y): 25 35
Cities near query point: [(20, 30), (40, 10)]
Nearest city to query point: (20, 30)