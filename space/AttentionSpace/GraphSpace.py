from ..abstraction import Graph
from ..utils import Visit
from ..ChangeListener import emit
from ..abstraction import Node
from .NodeAttention import NodeAttention

class GraphSpace(Graph, Visit):
  def __init__(self):
    super(GraphSpace, self).__init__()
  
  def on_forward_neighbor(self, id : int):
    try:
      node = self.vertices[id]
      node.forward_neighbor()
    except Exception as e:
      # Trường hợp id chưa tồn tại sẽ gọi hàm này
      print(e)
  
  def add_vertice(self, vertice : NodeAttention):
    assert isinstance(vertice, NodeAttention)

    vertice.id = len(self.vertices)
    self.vertices.append(vertice)  
    
    emit(name="vertice", vertices=self.vertices)