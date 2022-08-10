import torch
import torch.nn as nn
import torch.optim as optim

import torchvision
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import torchvision.transforms as transform
from torch.utils.tensorboard import SummaryWriter

class Discriminator(nn.Module):



def GetVersion(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(torch.__version__)
    print(torch.version.cuda)
    print(torch.backends.cudnn.version())
    print("GPU:",torch.cuda.is_available())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GetVersion('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
