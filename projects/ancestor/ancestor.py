class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def check_parents(ancestors, vertex):
    c = set()
    for parent, child in ancestors:
        # Add each child from ancestors list to the set
        c.add(child)
        # Check if the child we're looking at has a parent, if so, return true...otherwise...return false
    if vertex in c:
        return True
    else:
        return False      

def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    visited = set()
    # create a path list that will hold 
    path = []
    # If the node we start at has no parents, return -1
    if check_parents(ancestors, starting_node) is False:
        return -1
    # Otherwise, add the starting node to Stack and kick off the loop
    s.push(starting_node)
    while s.size() > 0:
        # Remove item from Queue and store as a value
        value = s.pop()
        if value not in visited:
            visited.add(value)
            # Next, check if that value has parents by calling the check_parents function
            if check_parents(ancestors, value) is True:
                path = []
                for p, c in ancestors:
                    # If the child equals the value of the starting node...
                    if c == value:
                        # Add the parent of that child to the Queue (This essentially works it's way up the graph)
                        s.push(p)
                        # Add the parents to the path array
                        path.append(p)
    # When the loop ends, return the smallest of the parents if there are multiple.
    return min(path)

result = earliest_ancestor(test_ancestors, 6)  
print(result)         
    

        




