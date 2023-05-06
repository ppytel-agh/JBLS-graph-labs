import random
import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from random import random as rand

#############################################################
def Draw_Graph(G, colors):
  pos = nx.circular_layout(G)
  nx.draw(G, pos=pos, with_labels=True, node_color=colors, connectionstyle='arc3, rad=0.2', node_size=200)
  labels = nx.get_edge_attributes(G,'weight')
  for (n1, n2), label in labels.items(): 
    (x1, y1) = pos[n1]
    (x2, y2) = pos[n2]
    (x0, y0) = ((x1 + x2) / 2, (y1 + y2) / 2)
    r = math.sqrt(math.pow(x2 - x0, 2) + math.pow(y2 - y0, 2))
    alfa = math.atan2(y0 - y2, x0 - x2) + math.pi/2
    (x, y) = (x0 + 0.2 * r * math.cos(alfa), y0 + 0.2 * r * math.sin(alfa))
    plt.text(x, y, label, fontweight=800, fontsize=12)
  plt.show()
#############################################################
def DFS_visit(v,G,d,f,t):
  t = t + 1
  d[v] = t
  u_list = [edge[1] for edge in G.edges if edge[0] == v]
  for u in u_list:
    if d[u] == -1:
      t = DFS_visit(u,G,d,f,t)
  t = t + 1
  f[v] = t
  return t
#############################################################
def Components_R(nr,v,G,comp):
  u_list = [edge[1] for edge in G.edges if edge[0] == v]
  for u in u_list:
    if comp[u] == -1:
      comp[u] = nr
      Components_R(nr,u,G,comp)
#############################################################
def Init(G,s,d,p):
  for v in G.nodes:
    d[v] = 10000
    p[v] = None
  d[s] = 0
#############################################################
def Relax(u,v,w,d,p):
  if d[v] > d[u] + w[u][v]:
    d[v] = d[u] + w[u][v]
    p[v] = u
#############################################################
def Dijkstra(G,w,s):
  S = []
  d = {}
  p = {}
  Init(G,s,d,p)
  while len(S) < len(G.nodes):
    temp_d = {key: d[key] for key in set(G.nodes) - set(S)}
    u = min(temp_d, key=temp_d.get)
    S.append(u)
    v_list = [edge[1] for edge in G.edges if edge[0] == u and edge[1] not in S]
    for v in v_list:
      Relax(u,v,w,d,p)
  return d
#############################################################
def Create_DiGraph(n,p):
  vertices = list(range(1, n+1))
  edges = []
  weights = {}
  for vertex in vertices:
    weights[vertex] = {}
    for other_vertex in vertices:
      if random.uniform(0, 1) <= p and vertex != other_vertex:
        w =  random.randint(-5, 10)
        edge = (vertex, other_vertex, w)
        edges.append(edge)

  G = nx.DiGraph()
  G.add_nodes_from(vertices)
  G.add_weighted_edges_from(edges)
  colors = [(0,1,1) for _i in range(1, n+1)]
  Draw_Graph(G, colors)

  labels = nx.get_edge_attributes(G,'weight')
  for (v, u), label in labels.items(): 
    weights[v][u] = label

  return G, weights
#############################################################
def Kosaraju(G):
  d = {}
  f = {}
  for v in G.nodes:
    d[v] = -1
    f[v] = -1

  t = 0
  for v in G.nodes:
    if d[v] == -1:
      t = DFS_visit(v,G,d,f,t)

  Transposed_G = nx.DiGraph()
  Transposed_G.add_nodes_from(G.nodes)
  reversed_edges = []

  for edge in G.edges:
    reversed_edges.append(edge[::-1])
  Transposed_G.add_edges_from(reversed_edges)

  f = dict(reversed(sorted(f.items(), key=lambda item: item[1])))
  nr = 0
  comp = {}
  for v in G.nodes:
    comp[v] = -1
  for v in f:
    if comp[v] == -1:
      nr = nr + 1
      comp[v] = nr
      Components_R(nr,v,Transposed_G,comp)

  colors = dict(zip(list(range(1,nr+1)), [(uniform(0.3,1.0),uniform(0.3,1.0),uniform(0.3,1.0)) for i in range(1,nr+1)]))
  Draw_Graph(G, [colors[val] for val in comp.values()])
  return nr == 1
#############################################################
def Bellman_Ford(G,w,s,d):
  p = {}
  Init(G,s,d,p)
  for i in range(1,len(G.nodes)):
    for u,v in G.edges:
        Relax(u,v,w,d,p)
  for u,v in G.edges:
    if d[v] > d[u] + w[u][v]:
      return False
  return True
#############################################################
def Add_s(G,w,s):
  G0 = G.copy()
  G0.add_node('s')
  w0 = w.copy()
  w0['s'] = {}
  for v in G.nodes:
    w0['s'][v] = 0
    G0.add_edge(s, v, weight=0)
  return G0,w0
#############################################################
def Johnson(G,w):
  d = {}
  h = {}
  wb = {}
  s = 's'
  G0,w0 = Add_s(G,w,s)
  if Bellman_Ford(G0,w0,s,d) == False:
    return []
  else:
    for v in G0.nodes:
      h[v] = d[v]
      wb[v] = {}
    for u,v in G0.edges:
      wb[u][v] = w0[u][v] + h[u] - h[v]
  D = {}
  for u in G.nodes:
    D[u] = {}
    db = Dijkstra(G,wb,u)
    for v in G.nodes:
      D[u][v] = db[v] - h[u] + h[v]
  return np.array([[D[v][u] for u in G.nodes] for v in G.nodes])
#############################################################
# 1
n = 4
p = 0.5
G,w = Create_DiGraph(n,p)

# 2
StronglyConnected = Kosaraju(G)
print('Weights list')
for v in G.nodes:
  print(v, ' --> ',w[v])

# 3 + 4
if StronglyConnected:
  D = Johnson(G,w)
  print(D)

#############################################################
""" example 1
edges = [(1,2,6),(1,3,3),(1,5,-1),
        (2,1,10),(2,3,-5),(2,4,-4),(2,5,4),(2,7,4),
        (3,6,2),
        (4,2,5),(4,7,9),
        (5,7,-4),
        (6,2,9),
        (7,6,4)]
"""

""" example 2
edges = [(1,2,-1),(1,3,-4),
        (2,1,4),
        (3,2,2)]
"""

""" example 3
edges = [(1,7,''), 
        (2,1,''), (2,3,''), (2,6,''), (2,7,''), 
        (3,2,''), (3,6,''), 
        (4,3,''), (4,5,''), 
        (5,3,''), 
        (6,5,''),
        (7,1,'')]
"""
