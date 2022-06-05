import torch.nn as nn
from ..abstraction import Label

class NodeLabel(Label):
  def __init__(self, get_attention : func):
    super(NodeLabel, self).__init__(vl)
    
    assert callable(get_attention)
    
    self.get_attention = get_attention
    
  def run(self, x : torch.Tensor):
    pass