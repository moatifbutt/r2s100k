"""
We will use the FCN ResNet50 from the PyTorch model. We will not
use any pretrained weights. Training from scratch.
"""

import torchvision.models as models
import torch.nn as nn

def model(pretrained, requires_grad):
    model = models.segmentation.deeplabv3_resnet101(
        pretrained=pretrained, progress=True)

    if requires_grad == True:
        for param in model.parameters():
            param.requires_grad = True
    elif requires_grad == False:
        for param in model.parameters():
            param.requires_grad = False

    # change the classification FCNHead and make it learnable
    model.classifier[4] = nn.Conv2d(256, 15, kernel_size=(1, 1))

    # change the aux_classification FCNHead and make it learnable
    model.aux_classifier[4] = nn.Conv2d(256, 15, kernel_size=(1, 1))
    
    return model


model = model(pretrained=True, requires_grad=True)
print(model)
