'''
A recursive code for DFS for directed and undirected edges.
'''
visited=[]    
#Definition of DFS 
def DFS(graph,node):
    
    #If the node is not in the visited list, then enter the loop else go back to the previous recursive call
    if node not in visited:
        visited.append(node)
        for i in graph[node]:
            DFS(graph,i)
    else:
        return
    
#Printing the the order of DFS 
def printVisited():
    print(visited)    
        
if __name__=="__main__":
    '''
    Declaration of the graph. When a node does not have any edge 
    leading to another edge, please insert it as an empty list. For example 5:[]
    '''
    graph = {
     1: [2,3],
     2: [4,5],
     3: [],
     4: [],
     5: []
    }
    #1 is the root node
    DFS(graph,1)
    printVisited()
