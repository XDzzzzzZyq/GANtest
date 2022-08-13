import torch

tensor = torch.tensor([[1,2,3],[3,4,5]],dtype=torch.float32)
#print(tensor)
#print(tensor.shape)

x= torch.empty(size=(4,4))
print(x)

x=x.uniform_(0,1)
x=x.normal_(0,1)
print(x)

x= torch.ones(4)
x*=5
print(x)

x=torch.rand(5)
x=torch.rand((1,5))
print(x)

x = torch.ones((1,5))
print(x)

for index,val in enumerate(*x):
    print(index,val)
import numpy as np