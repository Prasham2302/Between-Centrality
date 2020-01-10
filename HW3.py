"""
NAME = PRASHAM NARAYAN
ROLL NO. = 2018359
SECTION = B
GROUP = 8
"""
import ast
def graph(vertices,edges):
    """
    Makes the virtual Graph using vertices and edges.

    Args:
        Vertices: Vertices of the graph.
        edges: Edges of the graph.

    Returns:
        a Dictionary with  vertices as key and all its connecting vertices
        as list in it.
    """

    graph = {k:[] for k in vertices}
    for i in vertices:
        for j in edges:
            u,v = j
            if u==i:
                graph[i].append(v)
            elif v==i:
                graph[i].append(u)
    return graph
def shortest_path(graph, start, end):
    """
   Finds all shortest paths between start_node and end_node
    Args:
    graph: Virtual graph
        start: Starting node for paths
        end: Destination node for paths

    Returns:
        A list of path, where each path is a list of integers.
    """
    traversed = []
    all = []
    queue = []
    queue.append([start])
    while len(queue) > 0:
        temporary=queue.pop(0)
        node=temporary[-1]
        path=temporary
        if node not in traversed:
            in_nodes = graph[node]
            for i in range (0,len(in_nodes),+1):
                #gets the current path
                new_path=[]
                new_path.extend(path)
                new_path.append(in_nodes[i])
                queue.append(new_path)
                if in_nodes[i]==end:
                    all.append(new_path)
                    #adding the final paths to a list
            traversed.append(node)
            
            #adding the node that has been used in list
    i = 0
    if len(all)>1 :
        min = len(all[0])
        while i < len(all):
            if len(all[i])<min:
                min = len(all[i])
                i+=1
            elif len(all[i])==min:
                i+=1
            elif len(all[i])>min:
                all.pop(i)
    return all
def make_pairs(vertices):
    """
    Make pairs using the vertices.

    Args:
        Vertices: Vertices of the Graph

    Returns:
        A nested list containing all the pairs.
    """
    pairs = []
    for i in range(0,len(vertices),+1):
        for j in range (i+1,len(vertices),+1):
            pairs.append([vertices[i],vertices[j]])
    return pairs
def betweeness(number,pairs,gr,vertices):
    """
    Find betweenness centrality of the given node

    Args: 
        number: Node to find betweenness centrality of.
        pairs: All possible pairs of nodes required.
        gr: Virtual Graph
        vertices: All the vertices of the graph.

    Returns:
        Single floating point number, denoting betweenness centrality
        of the given node
    """
    i=0
    while i < len(pairs):
        if number in pairs[i]:
            pairs.pop(i)
        else :
            i+=1
    paths = {}
    for i in range (0,len(pairs),+1):
        paths[pairs[i][0],pairs[i][1]]=(shortest_path(gr,pairs[i][0],pairs[i][1]))
    list1={}
    sum=0
    for i in range (0,len(pairs),+1):
        countX=len(paths[pairs[i][0],pairs[i][1]])
        countY=0
        for j in range (0,len(paths[pairs[i][0],pairs[i][1]]),+1):
            temp = []
            temp.extend(paths[pairs[i][0],pairs[i][1]][j])
            if number in temp:
                countY+=1           
        list1[pairs[i][0],pairs[i][1]]=countY/countX
        sum = sum + (countY/countX)
    return (sum)
vertices = input("Enter the vertices : ",)
edges = input("Enter the edges : ",)
vertices = ast.literal_eval(vertices)
edges = ast.literal_eval(edges)
#vertice = [1, 2, 3, 4]
#edges = [(1, 2), (1, 3), (1, 4)]
gr=graph(vertice,edges)
print ("Virtual Graph : ",gr)
bet = {}
i=0
while i<len(vertice):
    pairs = make_pairs(vertice)
    bet[vertice[i]]=betweeness(vertice[i],pairs,gr,vertice)
    i+=1
print ("Betweenness Centrality : ", bet)
std_bet={k:None for k in vertice}
N=len(vertice)
z=((N-1)*(N-2))/2
i=0
while i<N:
    std_bet[vertice[i]]=bet[vertice[i]]/z
    i+=1
print ("Standardized Betweenness Centrality : ",std_bet)
top_nodes=[]
max=0
i=0
while i<N:
    if max<std_bet[vertice[i]]:
        max=std_bet[vertice[i]]
    i+=1
i=0
while i<N:
    if std_bet[vertice[i]]==max:
        top_nodes.append(vertice[i])
    i+=1
print ("top k nodes :",top_nodes)