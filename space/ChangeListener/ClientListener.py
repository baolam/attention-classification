from . import observer

class ClientListener():
  def __init__(self):
    self.__event = dict()
    
  def on(self, event, func):
    assert callable(func)
    self.__event[event] = func
  
  def del_listener(self, event):
    self.__event[event] = None
    del self.__event[event]
  
  def emit(self, **kwargs):
    observer.emit(**kwargs)
  
  def running(self, **kwargs):
    _evt = kwargs.get("name")
    if _evt == None:
      return
    for event, func in self.__event.items():
      if event == _evt:
        func(**kwargs)  
  
  @staticmethod
  def add_listener(listener):
    observer.add(listener)