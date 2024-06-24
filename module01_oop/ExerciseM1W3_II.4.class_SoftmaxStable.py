# Phần trắc nghiệm - Câu hỏi 4
import torch
import torch . nn as nn

class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition

data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
assert round(output[-1].item(), 2) == round(0.67, 2)
print(output)

# Đáp án là b) [0.0900, 0.2447, 0.6652]