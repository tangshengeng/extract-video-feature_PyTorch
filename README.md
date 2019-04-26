# extract-video-feature_PyTorch
Pytorch implementation of extracting frame-level features of video by a 2D CNN(ResNet-18). This project is made by Shengeng Tang.
Hefei University of Technology, Ph.D candidate.

In this project, we (1) first split the video into frames, (2) then extract the frame-level features, and (3) finally combine the frame-level features into clip-level features for alignment and fusion with other features.

# Requirements
See the installation instruction for a step-by-step installation guide. See the server instruction for server settup.

* Install cuda-8.0
* Install cudnn v5.1
* Download PyTorch for python-2.7 and clone the repository.
* Download PyTorch-3.5 for using further pretrained libraries with anaconda3.

``` pip install http://download.pytorch.org/whl/cu80/torch-0.1.12.post2-cp27-none-linux_x86_64.whl
``` pip install torchvision
``` git clone https://github.com/meliketoy/resnet-fine-tuning.pytorch
