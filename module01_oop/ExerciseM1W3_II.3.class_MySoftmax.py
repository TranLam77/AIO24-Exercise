# Phần trắc nghiệm - Câu hỏi 3
import torch
import torch . nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
    ### Your Code Here
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)
    ### End Code Here

data = torch.Tensor([1, 2 , 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[0].item(), 2) == round(0.00)
print(output)

# Đáp án là c) [0., 0., nan]