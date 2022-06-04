from abc import ABC
from typing import List
from . import Node
import torch

'''
  Lưu trữ đỉnh --> Lưu trữ id
  Lưu trữ cạnh --> Tổ chức lưu trữ theo danh sách cạnh
'''
class Graph(ABC):
  def __init__(self):
    super(Graph, self).__init__()
    
    self.vertices : List[Node] = [] # Tập các đỉnh
    
  def build_graph(self, n : int, m : int, algorithm):
    """Gọi hàm này để xây dựng, tạo nên một đồ thị mới

    Args:
      n (int) : ,
      m (int) : ,
      algorithm (_type_): _description_

    Raises:
      ValueError: _description_
    """
    if callable(algorithm) == False:
      raise ValueError("algorithm must be func")
  
  def add_vertice(self, vertice : Node):
    # Tạm giả sử là đỉnh không trùng lắp
    self.vertices.append(vertice)
    
  def on_forward_neighbor(self, id : int):
    raise NotImplementedError("hàm on_forward_neighbor phải được cài đặt")
  
  def init_node(self):
    raise NotImplementedError("hàm init_node phải được cài đặt")