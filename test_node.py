from space.abstraction.Node import Node
import torch

class MyNode(Node):
  def __init__(self, da):
    super(MyNode, self).__init__(da)

my_node = MyNode(512)
x = torch.randn((2, 512))

print (my_node(x))