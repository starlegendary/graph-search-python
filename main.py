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
print(dfs(graph,'A','G'))