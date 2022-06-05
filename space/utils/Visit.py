from ..ChangeListener import ClientListener

class Visit():
  def __init__(self):
    self.client = ClientListener()

    self.client.on("vertice", self.__handling_vertice)
    # Thêm người lắng nghe
    ClientListener.add_listener(self.client)
    
  def __handling_vertice(self, **kwargs):
    vertices = kwargs.get("vertices")
    visited = [False] * len(vertices)
    