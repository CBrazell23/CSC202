from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

#Class for the vertices
class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.edges = 0
        self.visited = False
        self.color = "NA"

    def __repr__(self):
        return("ID: {}\nAdjList: {}\nEdges: {}\nVisited: {}\nColor: {}".format(self.id, self.adjacent_to, self.edges, self.visited, self.color))

#Class for the graph
class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        infile = open(filename)
        lst = infile.readlines()
        self.adjList = []
        verts = []
        for i in range(len(lst)):
            eachLine = lst[i].split()
            for x in eachLine:
                verts.append(x)

        for i in range(0, len(verts), 2):
            if(verts[i] not in self.adjList):
                self.adjList.append(Vertex(verts[i]))
            if(verts[i + 1] not in self.adjList):
                self.adjList.append(Vertex(verts[i + 1]))

        for i in range(len(self.adjList)):
            for j in range(1, len(verts), 2):
                if(verts[j] == self.adjList[i].id):
                    self.adjList[i].edges += 1
                if(verts[j - 1] == self.adjList[i].id):
                    self.adjList[i].adjacent_to.append(verts[j])
        infile.close()

    # Function that adds vertex to graph if it's not in the graph
    # int -->
    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        alreadyIn = False
        for i in range(len(self.adjList)):
            if(self.adjList[i].id == key):
                alreadyIn = True
        if(not alreadyIn):
            self.adjList.append(Vertex(key))

    # Function that returns vertex object associated with id
    # int --> Vertex
    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        contains = -1
        for i in range(len(self.adjList)):
            if (self.adjList[i].id == key):
                contains = i
        if(contains == -1):
            return None
        else:
            return(self.adjList[contains])

    # Function that adds edge between two vertices
    # Vertex, Vertex -->
    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        if(v2.adjacent_to.count(v1) == 0):
            v2.adjacent_to.append(v1.key)
            v1.edges += 1
        if(v1.adjacent_to.count(v2) == 0):
            v1.adjacent_to.append(v2.key)
            v2.edges += 1

    # Function that returns list of ids for the vertices in a graph
    # --> list
    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        lst = []
        for i in range(len(self.adjList)):
            lst.append('v' + self.adjList[i].id[1:])
        lst.sort(key=lambda x: x[1:]) # Sorts by vertex number
        return lst

    # Function that returns list of lists of vertices in the connected component
    # --> list
    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''

        LoL = []
        vertLst = self.get_vertices()
        stk = Stack(len(self.adjList))

        for i in range(len(vertLst)):
            if(self.get_vertex(vertLst[i]).visited == False):
                stk.push(vertLst[i])
                lst = [vertLst[i]]
                self.get_vertex(vertLst[i]).visited = True
                while(not stk.is_empty()):
                    temp = stk.pop()
                    for x in self.get_vertex(temp).adjacent_to:
                        if(self.get_vertex(x).visited == False):
                            stk.push(x)
                            lst.append(x)
                            self.get_vertex(x).visited = True
                LoL.append(lst)
        for i in range(len(LoL)):
            sorted = []
            for j in range(len(LoL[i])):
                sorted.append('v' + LoL[i][j][1:])
            lst.sort(key=lambda x: x[1:]) #Sorts by vertex number
            LoL[i] = sorted
        for i in range(len(vertLst)):
            self.get_vertex(vertLst[i]).visited = False
        return LoL


    # Function that determines whether or not a graph is bicolorable
    # --> bool
    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        LoL = self.conn_components()
        q = Queue(len(self.adjList))

        for i in range(len(LoL)):
            for j in range(len(LoL[i])):
                q.enqueue(LoL[i][j])
                if(self.get_vertex(LoL[i][j]).color == "NA"):
                    self.get_vertex(LoL[i][j]).color = "Red"
                while(not q.is_empty()):
                    temp = q.dequeue()
                    for z in range(len(self.get_vertex(temp).adjacent_to)):
                        adj = self.get_vertex(temp).adjacent_to[z]
                        if(self.get_vertex(adj).color == "NA"):
                            if(self.get_vertex(temp).color == "Red"):
                                self.get_vertex(adj).color = "Black"
                            elif(self.get_vertex(temp).color == "Black"):
                                self.get_vertex(adj).color = "Red"
                            q.enqueue(adj)
                        elif(self.get_vertex(adj).color == self.get_vertex(temp).color): #Determines if adjacent vertices are the same color
                            return False
        return True