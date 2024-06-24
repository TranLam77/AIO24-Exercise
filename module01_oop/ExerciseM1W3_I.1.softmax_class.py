import torch
import torch.nn as nn

# Softmax class
class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.exp(x)/torch.sum(torch.exp(x))

# Softmax_stable class
class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x)
        return torch.exp(x-c)/torch.sum(torch.exp(x-c))

# input data
data = torch.tensor([1, 2, 3])

# test Softmax class
softmax = Softmax()
output = softmax(data)
print(output)

# test Softmax_stable class
softmax_stables = SoftmaxStable()
output = softmax_stables(data)
print(output)