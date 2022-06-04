# Không gian tính chất
import torch.nn as nn
import torch

'''
  Tính toán giá trị
'''
class NatureValue(nn.Module):
  def __init__(self, da):
    super(NatureValue, self).__init__()
    
    self.w_v = torch.rand((da), requires_grad=True)
    self.b = torch.rand((da), requires_grad=True)
  
  def forward(self, x : torch.Tensor) -> torch.Tensor:
    return self.w_v * x + self.b

'''
  Xác định có tồn tại tính chất n hay không
'''
class NatureAttention(nn.Module):
  def __init__(self, da):
    super(NatureAttention, self).__init__()
    
    self.linear = nn.Linear(da, 1, bias=True)
    self.n = torch.rand((da), requires_grad=True)
  
  def forward(self, x : torch.Tensor) -> torch.Tensor:
    x = self.n * x
    x = self.linear(x)
    return torch.sigmoid(x)

'''
  Tính toán
'''
class NatureSpace(nn.Module):
  def __init__(self, da):
    super(NatureSpace, self).__init__()
    
    self.attention = NatureAttention(da)
    self.value = NatureValue(da)
  
  def forward(self, x : torch.Tensor) -> torch.Tensor:
    n = self.attention(x)
    y = self.value(x) * n
    return y, n