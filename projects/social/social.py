import sys
sys.path.insert(0, '../graph')
from util import Queue
import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}  # Nodes
        self.friendships = {} # Edges

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # self.count = 0
        # Add users
        for user_i in range(0, num_users):
            self.add_user(f"User {user_i}")
        # Create friendships
        # Generate all possible friendship combinations (We can put them in a list)
        possible_friendships = []
        # Need to avoid duplicates by always starting at the 'next' user_id
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # print(possible_friendships, 'before randomize')
        random.shuffle(possible_friendships)
        # print(possible_friendships, 'after randomize')
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            # self.count += 1
            # print(self.count)
    # Should probably do a BFT for this
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Used to mark a user in the graph as visited, key would be the user visited, and value could be shortest path to that user
        # Initialize a Queue where we will track graph nodes
        q = Queue()
        # Add the current user to the Queue
        q.enqueue([user_id])
        # While the Queue is populated, we need to dequeue the item on it
        while q.size() > 0:
            value = q.dequeue()
            node = value[-1]
            if node == user_id:
                visited[node] = ['X']
            if node not in visited:
                visited[node] = value
            for friend in self.friendships[node]:
                n = list(value)
                n.append(friend)
                if friend not in visited:
                    q.enqueue(n)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print(sg.friendships)
    connections = sg.get_all_social_paths(2)
    print(connections, 'connections')
