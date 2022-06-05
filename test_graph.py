from space import GraphSpace
from space import NodeAttention
from space import end_changging_listener

try:
  da = 512
  a = NodeAttention(da)
  b = NodeAttention(da)
  c = NodeAttention(da)
  d = NodeAttention(da)

  graph = GraphSpace()

  graph.add_vertice(a)
  graph.add_vertice(b)
  graph.add_vertice(c)
  graph.add_vertice(d)

  a.update_neighbors([1, 3])
  b.update_neighbors([0, 3])
  c.update_neighbors([1])
  
  n = input()
  end_changging_listener()
except Exception as e:
  end_changging_listener()
  print(e)
