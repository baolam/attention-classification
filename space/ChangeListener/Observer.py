import threading
from queue import Queue
from typing import Set

class Observer:
  def __init__(self):
    self.__listener = set()
    self.queue = Queue()
    
    self.continous_running = True
    
    self.t = threading.Thread(name="observing_changing_variable", target=self.__running, daemon=False)
    self.t.start()
      
  def add(self, listener):
    self.__listener.add(listener)
  
  def remove(self, listener):
    self.__listener.remove(listener)
  
  def emit(self, **kwargs):
    """Phát sự kiện
    """
    self.queue.put(kwargs)
    
  def __running(self):
    while self.continous_running:
      if not self.queue.empty():
        o = self.queue.get()
        for j in self.__listener:
          j.running(**o)