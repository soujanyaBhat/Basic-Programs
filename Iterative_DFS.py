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
       
def DFS(graph,node):
    visited=[] 
    s=stack()
    s.push(node)
    while s.size()!=0:
        node=s.pop()
        if node in visited:
           continue
        visited.append(node)
        for i in graph[node]:
           s.push(i)
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
    DFS(graph,"A")
