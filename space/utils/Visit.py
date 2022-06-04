from ..ChangeListener import ClientListener

class Visit(object):
  def __init__(self, name):
    self.name = name
    self.__client = ClientListener()

    # Thêm người lắng nghe
    ClientListener.add_listener(self.__client)