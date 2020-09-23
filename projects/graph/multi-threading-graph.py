# from graph import Graph
from numba import jit, cuda
from recordclass import recordclass
import profile
# class MyGraph(Graph): #Making MyGraph a child of Graph
class MyGraph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id]=set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices.keys():
            self.vertices[v1].add(v2)
        else:
            self.vertices[v1]=set(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    # def __init__(self):
    #     super().__init__() #inherit all Graph's properties and methods.
    # @jit(nopython=True, parallel=True)
    # @jit(nopython=True, parallel=False)
    def Trim_Search(self, start_node, end_node):
        self.deadPaths = {}
        validPaths = [] #using list to get an easy 'bestPath = min(validPaths)'
        # allPaths = {}
        # deadPaths = {'uh':'hmm'}
        @jit(nopython=False, parallel=True)
        def mapOptions(path,blockedNodes=set()):
            
            
            # TODO: ADD WEIGHTING OKAY (MENTION EDGES PLEASE)BECAYUSE OTHERWISE I WOULD FORGET THAT WEIGHT GOES TO EDGES AND NOT VERTICES BECAUSE THAT/S SILLY ALSO DEFINITELY NEED TO REMOVE EXTRANEOUS CODE BECAUSE REASONS MAYBE I DON'T KNOW UHM THANK YOU FOR DICTATING THIS ZOE, I'M TRYING TO FIGURE OUT HOW TO, YOU KNOW WHAT? MAYBE YOU COULD USE MY, MIRROR? NO, NO. OKAY, OKAY, YOU CAN INCLUDE THAT TOO, IF YOU WANT, BUT AFTER THIS YOU NEED TO STOP, PLEASE!????????????????????????????????????????????????????????
            #CHECK POTATO TYPE FOR MASHED,,, CHECK AGAINST MASH, HASH, BASH, GASH, SASH. craSSH CASH
            # eliminate branching where 
            """
                ### Long version of below ####
                path = [1,2,3] #test value
                options = [5,6] #test value
                mapped = [path+[option] for option in options]
                for map in mapped:
                    if str(map) not in deadPaths.keys():
                        mapped.pop(mapped.index(map))
                print(mapped) # returns [[1, 2, 3, 6]] (excluded 1,2,3,5)
                ###    End Long Version   ####
            """
            #recursive function to efficiently gather and compare all graphs
            # visited = set(path)
            if blockedNodes==None:
                blockedNodes=set()
            options = self.vertices[path[-1]].difference(blockedNodes.union(path))
            if end_node in options:
                validPaths.append(path+[end_node])
                # allPaths[len(allPaths.keys())]=
                options.remove(end_node)
                # print(f"FOUND THE END! {path+[end_node]}")
            else:
                mapped = [path+[option] for option in options]
                for map in mapped:
                    mapOptions(map,blockedNodes)
        path = [start_node] #test path
        # blocked = set([9999999999999])
        mapOptions(path=path, blockedNodes=set([999]))
        if len(validPaths)<1:
            print("NO PATH FOUND!")
            self.deadPaths={}
            return None
        else:
            short = min(validPaths, key=len)
            long = max(validPaths, key=len)
            print("Total paths = ",len(validPaths),"Shortest path = ",short, "Longest path =", long)
            print("ALL PATHS:",*validPaths,sep="\n")
            self.deadPaths={}
            return short
        # mapped = list(filter(lambda fmap: str(fmap) not in pathDict.keys(),[path+[option] for option in options]))

    def MakeAFile(self):
        from string import ascii_uppercase
        vdict = self.vertices.copy()
        convert = ascii_uppercase
        newdict = {}
        x = open("edges0.txt","x")
        for key in vdict:
            # newkey = convert[int(key)]
            # newdict[convert[int(key)]]=[convert[int(edge)] for edge in vdict[key]]
            for edge in vdict[key]:
                x.write(f"{key}\t{edge}\n")



if __name__ == '__main__':
    graph = MyGraph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # graph.add_vertex(1)
    # graph.add_vertex(2)
    # graph.add_vertex(3)
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(6)
    # graph.add_vertex(100)
    for i in range(0,101):
        graph.add_vertex(i)
        for j in range(i+1,i+4):
            graph.add_edge(i%101,j%101)
    # graph.add_vertex(8)
    # graph.add_vertex(100)
    # graph.add_edge(5, 3)
    # graph.add_edge(6, 3)
    # graph.add_edge(7, 1)
    # graph.add_edge(4, 7)
    # graph.add_edge(1, 2)
    # graph.add_edge(7, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(2, 3)
    # graph.add_edge(4, 6)
    # graph.add_edge(20, 100)
    # for i in range(13,22):
    #     graph.add_edge(i,(((i**2))%22))
    #     graph.add_edge((((i**2))%22),((i-i*2)%22))
    #     graph.add_edge((((i**2+1))%22),((i-i*2)%22))
    #     graph.add_edge((((i**2+2))%22),((i-i*2)%22))
    #     graph.add_edge((((i**2+3))%22),((i-i*2)%22))
    #     if i==0:
    #         pass
    # graph.add_edge(3, 6)
    # graph.add_edge(5, 3)
    # graph.add_edge(5, 9)
    # graph.add_edge(5, 10)
    # graph.add_edge(5, 11)
    # graph.add_edge(5, 13)
    # graph.add_edge(13, 9)
    # graph.add_edge(5, 14)
    print(graph.vertices)
    # graph.Trim_Search(1,100)
    # profile.run('graph.Trim_Search(1,100)')
    # graph.MakeAFile()
    graph.Trim_Search(start_node=1,end_node=100)
    # profile.run('graph.Trim_Search(1,100)')
    # profile.run('graph.bfs(1,100)')
    # profile.run('graph.bfs(1,20)')
    # print(graph.bfs(1, 100))
    # print(graph.bfs(1, 20))
    # graph.Trim_Search(1,7)
    # graph.Trim_Search(1,7)
    # graph.Trim_Search(1,7)