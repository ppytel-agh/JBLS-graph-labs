import random
import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from random import random as rand

#############################################################
def Draw_Graph(G, pos):
  nx.draw(G, pos=pos, with_labels=True, arrowsize=15, node_size=200)
  plt.show()

#############################################################
def Create_Flow_Network(n):
  if n < 2 or n > 4:
    print("Invalid number of layers")
    return

  #source
  previous_layer = ['s']
  vertices = ['s']
  edges = []
  pos = {}
  pos['s'] = (0,0)
  vertex_number = 1

  #layers
  for i in range(1,n+1):
    number_of_vertices = random.randint(2, n)
    current_layer = []
    for j in range(0,number_of_vertices):
      vertices.append(vertex_number)
      current_layer.append(vertex_number)  
      y = (number_of_vertices / 4) - j / 2 - 0.25
      pos[vertex_number] = (i, y)
      vertex_number+=1

    for vertex in previous_layer:
      index = random.randint(0, len(current_layer)-1)
      edges.append((vertex, current_layer[index]))

    v_list = [vertex for vertex in current_layer if vertex not in [edge[1] for edge in edges]]
    for vertex in v_list:
      index = random.randint(0, len(previous_layer)-1)
      edges.append((previous_layer[index], vertex))

    previous_layer = current_layer.copy()

  #random edges
  for i in range(0,2*n):
    v = random.randint(1,vertex_number-1)
    u = random.randint(1,vertex_number-1)
    while v == u or (u,v) in edges:
      v = random.randint(1,vertex_number-1)
      u = random.randint(1,vertex_number-1)
    edges.append((u,v))
  
  #sink
  vertices.append('t')
  pos['t'] = (n+1,0)
  for vertex in previous_layer:
    edges.append((vertex, 't'))

  #weights
  for i, (u,v) in enumerate(edges):
    w = random.randint(1, 10)
    edges[i] = (u,v,w)

  #graph
  G = nx.DiGraph()
  G.add_nodes_from(vertices)
  G.add_weighted_edges_from(edges)
  Draw_Graph(G, pos)
  return G

#############################################################
G = Create_Flow_Network(3)
