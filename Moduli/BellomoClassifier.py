from torch import nn
import torchvision.models as models
from torchvision.models.resnet import ResNet18_Weights

class BellomoClassifier(nn.Module):

    def __init__(self):
        super(BellomoClassifier, self).__init__()

        #self.resnet = models.resnet18(pretrained = True)
        self.resnet = models.resnet18(weights=ResNet18_Weights.DEFAULT)
        self.features = nn.Sequential(*list(list(self.resnet.children())[:-1])) #rimozione ultimo livello
        self.flatten = nn.Flatten()
        
        # Classificatore
        self.fc = nn.Sequential(
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256,22)
        )


    def forward(self,x):
        #Applichiamo le diverse trasformazioni in cascata 
        x = self.features(x)
        x = self.flatten(x)
        #x = self.fc(x.view(x.shape[0],-1))
        x = self.fc(x) 
        return x