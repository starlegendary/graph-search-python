graph = {'A': 'BCE',
         'B': 'ADE',
         'C': 'AFG',
         'D': 'B',
         'E': 'ABD',
         'F': 'C',
         'G': 'C'}

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