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

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            vert = q.dequeue()
            vertex = vert[-1]
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    return vert
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
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            x = s.pop()
            value = x[-1]
            if value not in visited:
                visited.add(value)
                if value == destination_vertex:
                    return x
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
        if visited == None:
            visited = set()
        if path == None:
            path = []
        if starting_vertex not in visited:
            copy = list(path)
            copy.append(starting_vertex)
            visited.add(starting_vertex)
            if starting_vertex == destination_vertex:
                return copy
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
