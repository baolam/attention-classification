import torch.nn as nn
import torch

def sd_activation(x : torch.Tensor, c = 1e-9, threshold = 0.5):
  sd = torch.std(x, axis=1)
  n = x.size()[1]
  v1 = sd + (n / (sd + c))
  v2 = (x - threshold).sum(axis = 1) - n * threshold
  return torch.sigmoid(v1 * v2)