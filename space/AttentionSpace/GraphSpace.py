from ..abstraction import Graph
from ..utils import Visit

class GraphSpace(Graph, Visit):
  def __init__(self):
    super(GraphSpace, self).__init__()
    
  def on_forward_neighbor(self, id : int):
    try:
      node = self.vertices[id]
      node.forward_neighbor()
    except InterruptedError:
      # Trường hợp id chưa tồn tại sẽ gọi hàm này
      pass