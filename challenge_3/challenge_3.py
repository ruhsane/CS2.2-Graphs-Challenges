#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""
import queue

class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # check if vertex is already a neighbor
        # if not, add vertex to neighbors and assign weight.
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    # def __str__(self):
    #     """output the list of neighbors of this vertex"""
    #     return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        return [ n.id for n in self.neighbors]

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        # return the weight of the edge from this
        # vertext to the given vertex.
        if vertex in self.neighbors:
            return self.neighbors[vertex]


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.directed = False
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0

    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # increment the number of vertices
        self.numVertices += 1
        # create a new vertex
        vert = Vertex(key)
        # add the new vertex to the vertex list
        self.vertList[key] = vert
        # return the new vertex
        return vert

    def get_vertex(self, key):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vertList:
            return self.vertList[key]

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        if f not in self.vertList:
        # add it
            self.add_vertex(f)
        if t not in self.vertList:
            self.add_vertex(t)

        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].
        f_vert = self.get_vertex(f)
        t_vert = self.get_vertex(t)

        f_vert.add_neighbor(t_vert, cost)

        self.numEdges += 1


    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def dfs_paths(self, start, goal):
        '''
            searches for path from start node to goal node and returns the path
        '''
        stack = [(start, [start])]
        visited = set()
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == goal:
                    return path
                visited.add(vertex)
                for neighbor in self.vertList[vertex].get_neighbors():
                    stack.append((neighbor, path + [neighbor]))


    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())

def make_graph_from_file(text_file):
    '''
    reads file and make it into a graph object with respective properties.
    '''

    # Create the graph
    graph = Graph()

    # Opens and Parses through the text file to set up Graph
    with open(text_file, "r") as open_file:

        line_counter = 1
        for line in open_file:

            clean_line = line.strip()

            if line_counter == 1:
                
                if clean_line.upper() == 'G':
                    graph.directed = False
                elif clean_line.upper() == 'D':
                    graph.directed = True
                else:
                    raise Exception("File must begin with G or D, found %s" % clean_line)

            # if we are at second line
            if line_counter == 2:
                # get the vertex keys that are seperated by commas and add them to graph
                for key in clean_line.split(","):
                    graph.add_vertex(key)

            elif line_counter > 2:
                # make an array of the connected edges with the weight, split by comma
                edge_list = line.strip("()\n").split(',')

                # first item in the list is the 'from' vertex
                from_v = edge_list[0]
                # second item in the list is the 'to' vertex
                to_v = edge_list[1]
                # third argument is the weight (optional)
                if len(edge_list) == 3:
                    weight = edge_list[2]
                else:
                    #set weight to 0 if there's no weight specified
                    weight = 0

                # add edge from 'from' to 'to' with 'weight'
                graph.add_edge(from_v, to_v, weight)
                # If it is a Graph and not a Digraph, add another edge in the opposite direction
                if graph.directed == False:
                    graph.add_edge(to_v,from_v,weight)

            # add to line counter after reading this line
            line_counter += 1
            
        return graph


import argparse

if __name__ == "__main__":
    '''
    Output: If there is a path between the vertices (T/F) and the vertices in that path.

    There exists a path between vertex 1 and 5: TRUE
    Vertices in the path: 1,2,3,5
    '''

    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    parser.add_argument("from_vert")
    parser.add_argument("to_vert")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")

    g = make_graph_from_file(args.filename)

    # path = g.breadth_first_search(args.from_vert, args.to_vert)
    # num_edge = len(path) - 1

    # print("Vertices in shortes path: ")
    # print(path)
    # print("Number of edges in shortest path: " + str(num_edge))
    # print(g.get_vertex(args.from_vert))

    path = g.dfs_paths(args.from_vert, args.to_vert)
    if path:
        print(f"There exists a path between vertex {args.from_vert} and {args.to_vert}: TRUE")
        print(f"Verticies in path: {path}")

    else:
        print(f"There exists a path between vertex {args.from_vert} and {args.to_vert}: FALSE")
