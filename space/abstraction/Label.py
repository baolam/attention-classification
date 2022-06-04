from typing import List
from abc import ABC
from ..utils import check_list_data_type
import torch

class Label(ABC):
  def __init__(self, vl : int):
    super(Label, self).__init__()
    assert isinstance(vl, int)
    
    # Đây là giá trị của label (hiểu giống như id)
    # Được trả ra khi tập các điều kiện là thỏa mãn
    self.vl = vl

    # Tập các điều kiện
    self.conditionals : List[int] = []
  
  def update_conditionals(self, conditionals : List[int]):
    assert isinstance(conditionals, list)
    assert check_list_data_type(conditionals, int)
    
    self.conditionals = conditionals
    
  def run(self, x : torch.Tensor):
    """Kiểm tra các điều kiện

    Args:
        x (torch.Tensor): _description_
    """
    raise NotImplementedError("hàm run phải được cài đặt")