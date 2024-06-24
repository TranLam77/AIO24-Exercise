# Phần trắc nghiệm - Câu hỏi 1
import torch
import torch.nn as nn

data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(),2) == round(0.09, 2)
print(output)


# Đáp án là c) [0.0900, 0.2447, 0.6652]