![](https://github.com/tangshengeng/extract-video-feature_PyTorch/blob/master/pytorch.png {width=400px height=40px})
# Extract Video Feature (PyTorch)
Pytorch implementation of extracting frame-level features of video by a 2D CNN(ResNet-18). This project is made by Shengeng Tang.
Hefei University of Technology, Ph.D candidate.

In this project, we (1) first split the video into frames, (2) then extract the frame-level features, and (3) finally combine the frame-level features into clip-level features for alignment and fusion with other features.

# Requirements
See the installation instruction for a step-by-step installation guide. See the server instruction for server settup.

* Install [cuda-8.0](https://developer.nvidia.com/cuda-downloads)
* Install [cudnn v5.1](https://developer.nvidia.com/cudnn)
* Download [PyTorch for python-2.7](https://pytorch.org/) and clone the repository.

```
pip install http://download.pytorch.org/whl/cu80/torch-0.1.12.post2-cp27-none-linux_x86_64.whl
pip install torchvision
git clone https://github.com/tangshengeng/extract-video-feature_PyTorch
```

# Split the Video into Frames
```
python video2frames.py
```
# Extract the Features
```
python extract_features.py
```
# Combine the Features
```
python framefeats2clipfeats.py
```
