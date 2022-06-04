import torch
from typing import List
from abc import ABC
from ..utils import check_list_data_type

class Node(ABC):
  def __init__(self, da):
    super(Node, self).__init__(da)
    
    # Một đỉnh được xác định bởi 1 tập các đỉnh liền kề  
    self.neighbors : List[int] = []  
    
  def update_neighbors(self, neighbors : List[int]):
    """Các đỉnh láng giềng

    Args:
      neighbors (List[int]): _description_
    """
    assert isinstance(neighbors, list)
    assert check_list_data_type(neighbors, int)
    
    self.neighbors = neighbors
  
  def forward_neighbor(self):
    """Lan truyền sang hàng xóm
    """
    raise NotImplementedError("hàm forward_neighbor phải được cài đặt")