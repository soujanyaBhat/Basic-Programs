'''
A simple BFS program using queue
'''
#Creating the queue data structure
class queue:
    def __init__(self):
        self.items=[]
    def push(self,data):
        return self.items.append(data)
    def pop(self):
        return self.items.pop(0)

#Defining the BFS algorithm
def BFS(graph,node):
    visited=[]
    q=queue()
    q.push(node)
    while len(q.items)!=0:
        n=q.pop()
        if n not in visited:
            visited.append(n)
            #Adding every path to the queue that exists from node 'n' to other nodes
            for i in graph[n]:
                q.push(i)
    print(visited)

if __name__=="__main__":
    
    graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
    }
    BFS(graph,"A")
