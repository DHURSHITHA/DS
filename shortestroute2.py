import heapq

class TransportNetwork:
    def __init__(self):
        self.locations = set()
        self.connections = {}

    def add_location(self, location_name):
        self.locations.add(location_name)
        self.connections[location_name] = []

    def add_connection(self, start_location, end_location, travel_duration):
        self.connections[start_location].append((end_location, travel_duration))
        self.connections[end_location].append((start_location, travel_duration))

def compute_shortest_paths(network, origin):
    priority_queue = []
    heapq.heappush(priority_queue, (0, origin))
    shortest_distances = {loc: float('inf') for loc in network.locations}
    shortest_distances[origin] = 0
    previous_locations = {loc: None for loc in network.locations}

    while priority_queue:
        current_distance, current_location = heapq.heappop(priority_queue)

        if current_distance > shortest_distances[current_location]:
            continue

        for neighbor, travel_time in network.connections[current_location]:
            new_distance = current_distance + travel_time
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance
                previous_locations[neighbor] = current_location
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return shortest_distances, previous_locations

def find_shortest_route(network, start, destination):
    shortest_distances, previous_locations = compute_shortest_paths(network, start)
    route = []
    current_location = destination

    while current_location is not None:
        route.append(current_location)
        current_location = previous_locations[current_location]
    
    route = route[::-1]
    return route, shortest_distances[destination]

def main():
    network = TransportNetwork()
    
    num_locations = int(input("Enter the number of locations: "))
    print("Enter the locations (one per line):")
    for _ in range(num_locations):
        location = input().strip()
        network.add_location(location)
    
    num_connections = int(input("Enter the number of connections between locations: "))
    print("Enter the connections (format: start_location end_location travel_time):")
    for _ in range(num_connections):
        start_location, end_location, travel_time = input().strip().split()
        network.add_connection(start_location, end_location, int(travel_time))
    
    start_location = input("Enter the starting location: ").strip()
    end_location = input("Enter the destination location: ").strip()
    
    route, travel_duration = find_shortest_route(network, start_location, end_location)
    
    route_str = ' -> '.join(route)
    print(f"Shortest route: {route_str}")
    print(f"Travel time: {travel_duration}")

if __name__ == "__main__":
    main()


output:
Enter the number of locations: 5
Enter the locations (one per line):
A
B
C
D
E
Enter the number of connections between locations: 6
Enter the connections (format: start_location end_location travel_time):
A B 1
A C 4
B C 2
B D 5
C D 1
D E 3
Enter the starting location: A
Enter the destination location: E
Shortest route: A -> B -> C -> D -> E
Travel time: 7

=== Code Execution Successful ===