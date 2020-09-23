"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        vset = frozenset(self.vertices.keys())
        node=starting_vertex
        bftpath = [node]
        queue = [edge for edge in self.vertices[node]]
        while len(queue) != 0:
            node = queue.pop(0)
            if node not in bftpath and node in vset:
                bftpath.append(node)
            queue.extend(vset.intersection(self.vertices[node].difference(set(bftpath))))
        print("bft:",bftpath)
        return(bftpath)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        vset = frozenset(self.vertices.keys())
        node=starting_vertex
        dftpath = [node]
        queue = [edge for edge in self.vertices[node]]
        while len(queue) != 0:
            node = queue.pop(-1)
            if node not in dftpath and node in vset:
                dftpath.append(node)
            queue.extend(vset.intersection(self.vertices[node].difference(set(dftpath))))
        print("dft:",dftpath)
        return(dftpath)
        # vset = set(self.vertices.keys())
        # node=starting_vertex
        # dftpath = [node]
        # queue = [edge for edge in self.vertices[node]]
        # while len(queue) != 0:
        #     #travel to first node
        #     node = queue.pop()
        #     vset.discard(node)
        #     if node not in dftpath and node in vset:
        #             dftpath.append(node)
        #     queue.extend(
        #         vset.intersection(
        #             self.vertices[node].difference(
        #                 set(dftpath)
        #             )
        #         )
        #     )
        #     # print(node,"\t",vset.intersection(self.vertices[node].difference(set(dftpath))),"\t",queue)
        # print("dft:",dftpath)
        # return(dftpath)
        # # vset = frozenset(self.vertices.keys())
        # # node=starting_vertex
        # # dftpath = [node]
        # # queue = [edge for edge in reversed(list(self.vertices[node]))]
        # # while len(queue) != 0:
        # #     #travel to first node
        # #     node = queue[-1]
        # #     queue.pop(-1)
        # #     if node not in dftpath:
        # #         if node in vset:
        # #             dftpath.append(node)
        # #         else:
        # #             print("Error: Vertex \"{node}\" does not exist in our graph.")
        # #     queue.extend(
        # #         reversed(
        # #             list(
        # #                 vset.intersection(
        # #                     self.vertices[node].difference(
        # #                         set(dftpath)
        # #                     )
        # #                 )
        # #             )
        # #         )
        # #     )

    def dft_recursive(self, starting_vertex):
        try:
            if len(starting_vertex)>1:
                path = starting_vertex
        except:
            path = [starting_vertex]
        lastpath = path
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        node = path[-1]
        Everything = False
        #get the first option that isn't already in our path
        options = self.vertices[node].difference(set(path))
        try:
            path.append(options[0])
        except:
            for node in path:
                options = self.vertices[node].difference(set(path))
                if options != set():
                    path.append(list(options)[0])
                    break
        if len(path)==len(self.vertices.keys()):
            print("dft_recursive:",path)
        else:
            self.dft_recursive(path)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        vset = frozenset(self.vertices.keys())
        valid_paths = []
        def bfsearch():
            node=starting_vertex
            bfspath = [node]
            queue = [edge for edge in self.vertices[node]]
            while len(queue) != 0:
                node = queue.pop(0)
                if node not in bfspath and node in vset:
                    bfspath.append(node)
                    if destination_vertex in self.vertices[node]:
                        print("#we found it!")
                        bfspath.append(destination_vertex)
                queue.extend(vset.intersection(self.vertices[node].difference(set(bfspath))))
            print("bfs:",bfspath)
            return(bfspath)
        
        # vset = set(self.vertices) #converting to set for overall performance gains
        # valid_paths =[] #to store the paths taken
        
        # def bfs_multi():
        #     nonlocal valid_paths
        #     node = starting_vertex
        #     current_path = [node]
        #     visited = set([node])
        #     queue = []
        #     #This will cut down on complexity by creating 'savepoints' to return to.
        #     branch_points = [0 for i in range(min(min(vset),0),max(vset)+1)] 
        #     #0 for all our nodes, will update with number of valid branches remaining.

        #     #since we won't entertain visiting the same node twice, our max path length is len(vset)
        #     while len(current_path)<=len(vset):
        #         if destination_vertex in self.get_neighbors(node):
                    
        #             #we found the destination. Time to do things then end this iteration.
        #             current_path.append(destination_vertex)
        #             valid_paths.append(current_path)
        #             print(f"Found a path to destination {destination_vertex}. Path={current_path}")
        #             break
        #         else:
                    
        #             branches = list(visited.difference(self.get_neighbors(node)))
        #             print(f"No destination found. Possible branches = {branches}")
        #             if len(branches)>0:
        #                 if len(branches)>1:
        #                     queue.update(branches[1:])
        #                     branch_points[node]=branches[1:]
        #                 node = branches[0]
        #                 current_path.append(node)
        #                 visited.add(node)
        # bfs_multi()
        # print(valid_paths)
        # # best_path = min(valid_paths)
        # # print(f"bfs: {best_path}")
        # # return best_path


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO
    def Trim_Search(self, start_node, end_node):
        deadPaths = {
            #these paths will be checked against to prevent repition
            '[1, 2, 3, 5]':set([3]), #test value
        }
        validPaths = [] #using list to get an easy 'bestPath = min(validPaths)'
        currPaths = {
            '[1, 2, 4]':set([6,7])
            #perhaps use dict.update() to modify these down the line?
        }
        def lookAhead(path):
            nonlocal currPaths
            options = self.get_neighbors(path[-1]).difference(blockedNodes)
            print(f"{str(path)}:{options}")
            # currPaths[path[-1]]=options
            return options
        @jit(target ="cuda")
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
            visited = set(path)
            if blockedNodes==None:
                blockedNodes=set()
            options = self.get_neighbors(path[-1]).difference(blockedNodes.union(path))
            if end_node in options:
                # print(f"FOUND THE END! {path+[end_node]}")
                validPaths.append(path+[end_node])
                options.remove(end_node)
            else:
                # print(f"node = {path[-1]}, options = {options} = ({self.get_neighbors(path[-1])} - {blockedNodes})")
                # print(options)

                mapped = list(filter(lambda fmap: str(fmap) not in deadPaths.keys(),[path+[option] for option in options]))
                # print(f"path = {path}, options = {options}, mappings={mapped}")
                #this shows, like, everything going on.
                for map in mapped:
                    mapOptions(map,(blockedNodes))
                    # if map != None:
                    #     # mapOptions(map,(blockedNodes.add(map[-1])))
                    #     mapOptions(map,(blockedNodes))
                    # else:
                    #     print("ARE WE DONE???")
                    #     pass
                return mapped
        path = [start_node] #test path
        mapOptions(path)
        if len(validPaths)<1:
            print("NO PATH FOUND!")
            return None
        else:
            
            print(f"Total paths = {len(validPaths)}, Shortest path = {min(validPaths, key=len)}, Longest path = {max(validPaths, key=len)}")
            print("ALL PATHS:",*validPaths,sep="\n")
            return min(validPaths, key=len)
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
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    # graph.add_vertex(8)
    # graph.add_vertex(100)
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
    # graph.add_edge(2, 100)
    # graph.add_edge(100,8)

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
