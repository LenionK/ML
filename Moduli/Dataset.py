import torch
from torch import Tensor
from torchvision import transforms
import numpy as np
import torch
from torch.utils.data.dataset import Dataset
from PIL import Image
from os import path



class ScenesDatabase(Dataset):
    def __init__(self,base_path,txt_list,transform = None, split = "first" , div = 2) :
        
        np.random.seed(5678) 
        torch.random.manual_seed(5678)

        self.base_path = base_path
        self.images = np.loadtxt(txt_list,dtype = str , delimiter= ' ')
        np.random.shuffle(self.images)

        if split != None:
            split_idx = len(self.images) // div
            if split ==  "first":
                self.images = self.images[:split_idx]
            elif split == "second":
                self.images = self.images[split_idx:]
                
        self.transform = transform
        
    def __getitem__(self, index):
        f,c = self.images[index]
        res = f.split('/')

        if res[7] == "":
           f = res[6] + '/' + res[7] + res[8] 
        else:
           f = res[6] + '/' + res[7]
           if res[7].split('.')[1] != "jpg":
            f = f + "jpg"

       #print(self.base_path,f)
  
        im = Image.open(path.join(self.base_path,f))

        if self.transform is not None: 
           im = self.transform(im)

        label = int(c)

        return {'image' : im, 'label':label}
    
    def getLabel(self,index):
        return int(self.images[index][1])

    def __len__(self):
        return int(len(self.images))
    