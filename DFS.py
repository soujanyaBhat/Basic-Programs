class stack:
    def __init__(self):
        self.items=[]
    def pop(self):
        return self.items.pop(0)
    def push(self,i):
        return self.items.insert(0,i)
    def top(self):
        return self.items[0]
    def size(self):
        return len(self.items)
visited=[] 
s=stack()
       
def DFS(graph,node):
    
    if node not in visited:
        s.push(node)
        visited.append(node)
        for n in graph[node]:
            DFS(graph,n)
    else:
        return
def printVisited():
    print(visited)    
        
if __name__=="__main__":
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
    DFS(graph,'A')
    printVisited()
