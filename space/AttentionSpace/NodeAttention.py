from ..abstraction import Node
from .NatureSpace import NatureSpace

class NodeAttention(Node, NatureSpace):
  def __init__(self, da):
    super(NodeAttention, self).__init__(da)
  
  def enable(self):
    """Được kích thích
    """
    pass
  
  def disable(self):
    """Không được kích thích
    """
    pass
  
  def forward_neighbor(self):
    """Lan truyền sang hàng xóm
    """
    pass