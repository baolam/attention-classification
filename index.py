import torch
from space.AttentionSpace import NatureSpace

x = torch.randn((1, 512))
naturespace = NatureSpace(512)

y, n = naturespace(x)
print(y.size())