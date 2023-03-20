import torch
import torch.nn as nn
import torch.nn.functional as F

class GeoDiff(nn.Module):
    def __init__(self):
        super().__init__()
        pass

    def forward(self, x):
        return x

if __name__ == '__main__':
    model = GeoDiff()

    x = torch.randn(3, 3)
    print(model(x))
