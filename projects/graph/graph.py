"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Insert a new vertex(node) into our dictionary(vertices)
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # add a connection from vertex(v1) to vertex(v2)
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        # This returns all of the connections that exist with regard to the vertex we're looking at(Whatever is passed into the function)
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Breadth first uses a Queue, so we need to initalize a q
        q = Queue()
        # Need to add our starting vertex to the Queue
        q.enqueue(starting_vertex)
        # Need to store visited vertexes somewhere so we can track where we've already been.
        visited = set()
        # Need to continue the BFT as long as the Queue is populated, once it's empty we break out
        while q.size() > 0:
            # Need to first remove the first item from the Queue by Dequeueing 
            x = q.dequeue()
            # If x is has not already been visited, then we want to print that out
            if x not in visited:
                print(x)
                # Add to visited after it's printed
                visited.add(x)
                # Loop over neighbors of the vertex currently being looked at, and add them to the queue and repeat logic until queue is empty
                for next_vertex in self.get_neighbors(x):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Initialize a stack to store vertexes that we will be looking at
        s = Stack()
        # Need to push the starting_vertex onto the stack
        s.push(starting_vertex)
        # Must store the vertexes we've visited so we can track where we are
        visited = set()
        # While the stack is populated, we need to pop the most recent vertex off the stack and check that vertex's neighbors
        while s.size() > 0:
            x = s.pop() 
            if x not in visited:
                print(x)
                # Add to visited before moving onto the next one
                visited.add(x)
                # Loop over neighbors and work our way down
                for next_vertex in self.get_neighbors(x):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initalize visited to a set when function is run
        if visited is None:
            visited = set()
        # Add the starting vertex to visited
        visited.add(starting_vertex)
        # Print
        print(starting_vertex)
        # Get all the possible connections for the starting vertex
        connections = self.get_neighbors(starting_vertex)
        # While there are connections...
        while len(connections) > 0:
            # Loop over them
            for next_vertex in connections:
                # For each connection, check if it has not been visited
                if next_vertex not in visited:
                    # If it hasn't, then run the function on that vertex, repeat until all vertexes have been visited.
                    self.dft_recursive(next_vertex, visited)
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # Initialize a Queue
        q = Queue()
        # Add the starting vertex to Queue
        q.enqueue([starting_vertex])
        # Initialize a visited set
        visited = set()
        # While Queue is not empty
        while q.size() > 0:
            # Dequeue whatever is on the Queue, and assign to vert
            vert = q.dequeue()
            vertex = vert[-1]
            # If vertex not visited
            if vertex not in visited:
                # add to visited
                visited.add(vertex)
                # if the vertex being looked at equals the destination, we've found what we want, return it.
                if vertex == destination_vertex:
                    return vert
                # Otherwise, Loop over vertex's neighbors and enqueue
                else:
                    for next_vertex in self.get_neighbors(vertex):
                        n = list(vert)
                        n.append(next_vertex)
                        q.enqueue(n)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Initialize a stack
        s = Stack()
        # Push starting vertex onto stack
        s.push([starting_vertex])
        # Initialize visited
        visited = set()
        # While stack is populated...
        while s.size() > 0:
            # Pop last item added off the stack
            x = s.pop()
            value = x[-1]
            # Check if it's in visited
            if value not in visited:
                # Add if not
                visited.add(value)
                # If value being looked at equals the target, return it out
                if value == destination_vertex:
                    return x
                # otherwise, Loop over the neighbors of value and add to stack, re-run until we've checked everything and stack is empty
                else:
                    for next_vertex in self.get_neighbors(value):
                        n = list(x)
                        n.append(next_vertex)
                        s.push(n)
    
    # def add_to_visited(self, value):
    #     visited = set()
    #     visited.add(value)
    
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initalize visited as an empty set
        if visited == None:
            visited = set()
        # Initialize path as an empty list
        if path == None:
            path = []
        # If the vertex being looked at is not in visited
        if starting_vertex not in visited:
            # Create a copy first, so we don't overwrite path back to None when calling the function on itself
            copy = list(path)
            # Add starting vertex to it
            copy.append(starting_vertex)
            # Add it to visited so we don't check it again
            visited.add(starting_vertex)
            # If the starting vertex equals the target, return the copy list
            if starting_vertex == destination_vertex:
                return copy
            # otherwise, loop over the starting vertex's neighbors, and run dfs_recursive on them, assign result to n and return it out when the stack empties.
            for next_vertex in self.get_neighbors(starting_vertex):
                n = self.dfs_recursive(next_vertex, destination_vertex, visited, copy)
                if n:
                    return n


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
