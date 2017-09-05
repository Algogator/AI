import sys

class queue:
   def __init__(self):
      self.l = []
   def add(self, item):
      self.l.append(item)
   def get(self):
      self.l.sort()
      return self.l.pop(0)
   def empty(self):
      if self.l:
         return False
      return True

class Graph:
   def __init__(self):
      self.vertices = {}
   def __iter__(self):
      return iter(self.vertices)
   def add_vertex(self,o,d,c):
      if o not in self.vertices:
         v = Vertex(o)
         self.vertices[o]=v
         v.add_neigh(d,c)
      else:
         self.vertices[o].add_neigh(d,c)

class Vertex:
   def __init__(self,node):
      self.id = node
      self.visited = False
      self.adj = {}

   def __str__(self):
      return str([x for x in self.adj])

   def add_neigh(self,dest,cost):
      self.adj[dest]=cost

   def __iter__(self):
      return iter(self.adj)

# find_route input_filename origin_city destination_city
# print 'Argument List:', sys.argv[1], sys.argv[2], sys.argv[3]

g = Graph()

f = open(sys.argv[1], 'r')
for line in f:
   if line == "END OF INPUT\n":
      break
   data = line.split()
   origin = data[0].lower()
   dest = data[1].lower()
   cost = int(data[2])
   g.add_vertex(origin, dest,cost)
   g.add_vertex(dest, origin, cost)

#for i in g.vertices.keys():
#   print i,"...",g.vertices[i],"=",g.vertices[i].adj.values()
q = queue()

#UCS

origin = sys.argv[2].lower()
dest = sys.argv[3].lower()
# print origin,dest
q.add((0,[origin]))
visited = []
found = False
while not q.empty():
   n = q.get()
   fringe = n[1]
   current = fringe[-1]
   if current in visited:
      continue
   visited.append(current)
   # print fringe
   if dest in fringe:
      print "distance:",n[0],"km"
      print "route:"
      for i in range(len(fringe)-1):
         print fringe[i], "to",fringe[i+1],g.vertices[fringe[i]].adj[fringe[i+1]],"km"
      found = True
      break
   cost = n[0]
   for neigh in g.vertices[current]:
      temp = fringe[:]
      temp.append(neigh)
     # print cost+g.vertices[current].adj[neigh], temp
      q.add((cost+g.vertices[current].adj[neigh], temp))
if not found:
   print "distance: infinity"
   print "route:"
   print "none"
