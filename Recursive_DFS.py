'''
A recursive code for DFS for directed and undirected edges.
'''
    
#Definition of DFS 
def DFS(graph,node):
    
    #If the node is not in the visited list, then enter the loop else go back to the previous recursive call
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            DFS(graph,n)
    else:
        return
    
#Printing the the order of DFS 
def printVisited():
    print(visited)    
        
if __name__=="__main__":
    '''
    Declaration of the graph. When a node does not have any edge 
    leading to another edge, please insert it as an empty list. For example "R":[]
    '''
    graph = {
    'A' : ['S','B'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
    }
    #'A' is the root node
    DFS(graph,'A')
    printVisited()
