graph = {'A': 'BCE',
         'B': 'ADE',
         'C': 'AFG',
         'D': 'B',
         'E': 'ABD',
         'F': 'C',
         'G': 'C'}
def fib(n, mem):
    if n >= len(mem):
        mem.append(fib(n-2, mem) + fib(n-1, mem))
    return mem[n]
print(fib(5,[1,1]))
def bfs(graph, src, tar):
    q = [src]
    e = []
    while q!= []:
        currpath = q.pop(0)
        currnode = currpath[-1]
        if currnode not in e:
          e.append(currnode)
          for nextnode in graph[currnode]:
              if nextnode == tar:
                  return currpath + nextnode
              q.append(currpath + nextnode)
    return None


def new_bfs(graph, src, tar):
    currpath = src #all path include the starting node
    explored = src #explored node as string
    tonext = {currpath:graph[src[-1]]} 
    #tonext = {path: all next node}
    while tonext!= {}:
      currpath = next(iter(tonext))
      #get first element in tonext
      for nextnode in tonext[currpath]:
          if nextnode not in explored:
              if nextnode == tar:
                  return currpath + nextnode
              tonext[currpath+nextnode] = graph[nextnode]
              #add all future move of newpath to tonext
              explored += nextnode
              #as nextnode not equal to tar, thus explored
      tonext.pop(currpath)
      #get rid of the curr path
    return None
def new_bfs2(graph, src, tar):
    allpath = ['']
    allnode = [src]
    explored = []
    while(allnode!=[]):

        allnext = allnode.pop(0)
        currpath = allpath.pop(0)
        for nextnode in allnext:
            if nextnode not in explored:
                nextpath = currpath+nextnode
                if nextnode == tar:
                    return nextpath
                allpath.append(nextpath)
                allnode.append(graph[nextnode])
                explored.append(nextnode)
    return None
def dfs(graph, src, tar):
    q = [src]
    e = []
    while q!= []:
        print(q)
        currpath = q.pop(0)
        currnode = currpath[-1]

        if currnode not in e:
          e.append(currnode)
          n = 0
          for nextnode in graph[currnode]:
              n += 1
              if nextnode == tar:
                  return currpath + nextnode
              elif n == 0:
                  q = q+ [currpath + nextnode]
              else:
                  q = [currpath + nextnode] + q
def new_bfs3(graph, src, tar):
    allpath = ['']
    allnode = [src]

    while(allnode!=[]):

        allnext = allnode.pop(0)
        currpath = allpath.pop(0)
        print(allnext)
        for nextnode in allnext:
            nextpath = currpath+nextnode
            if nextnode == tar:
                return nextpath
            graph = dict(
                  map(
                      lambda x: (x[0],''.join
                        (filter(lambda xx: xx!= nextnode, x[1]))
                      ), 
                  graph.items()
                )
            )
            
            allpath.append(nextpath)
            allnode.append(graph[nextnode])
            print(allnode)

    return None
def bfs3(graph, src, tar):
    q = [src]
    while q!= []:
        currpath = q.pop(0)
        currnode = currpath[-1]
        graph = dict(
              map(
                  lambda x: (x[0],''.join
                    (filter(lambda xx: xx!= currnode, x[1]))
                  ), 
              graph.items()
            )
        )
        graph = dict(filter(lambda x: x[0]))
        print(graph)
        for nextnode in graph[currnode]:
            if nextnode == tar:
                return currpath + nextnode
            q.append(currpath + nextnode)
    return None
class adj:
    def __init__(self, nodes):
        self.N = len(nodes)
        self.nodes = nodes

        self.toint = dict(zip(nodes,range(self.N)))
        #return to the position (1-n)of the node
        self.tosym = dict(zip(range(self.N),nodes))
        #return to the symbol of the node from position
        self.m = [[0]*self.N for i in range(self.N)]
        #adjacency matrix

    def edge(self,a,b):
        #a -> b
        self.m[self.toint[a]][self.toint[b]] += 1
        return self.m[self.toint[a]][self.toint[b]]

    #tonext:: string -> [string]
    def tonext(self,a):#get all next node a can go to
        allnext = self.m[self.toint[a]]
        rest = []
        for idx, value in enumerate(allnext):
            if(value > 0): rest.append(self.tosym[idx])
        return rest
    #tonext:: string, string -> [string]
    def bfs(self, src, tar): #normal bfs algorithm
        q = [src]
        e = []
        while q!= []:
            currpath = q.pop(0)
            currnode = currpath[-1]
            if currnode not in e:
              e.append(currnode)
              for nextnode in self.tonext(currnode):
                  if nextnode == tar:
                      return currpath + nextnode
                  q.append(currpath + nextnode)
        return None

    def alledge(self): return sum(map(sum,self.m))
    def high(self):
        rest = list(map(sum, self.m))
        return self.tosym[rest.index(max(rest))]




a = adj(['a','b','c','d'])

print(a.m)

a.edge('a','c')
a.edge('c','b')
a.edge('b','c')
a.edge('b','d')
a.edge('b','c')


print(a.m)
print(a.alledge())
print(a.bfs('a','d'))
print(a.high())
print(new_bfs3(graph,'A','G'))