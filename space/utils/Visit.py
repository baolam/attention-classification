from ..ChangeListener import ClientListener
from ..abstraction import Node
from typing import List

class Visit():
  def __init__(self):
    self.client = ClientListener()

    self.client.on("vertice", self.__handling_vertice)
    
    # Thêm người lắng nghe
    ClientListener.add_listener(self.client)
    
  def __handling_vertice(self, **kwargs):
    vertices : List[Node] = kwargs.get("vertices")
    visited = [False] * len(vertices)
    
    