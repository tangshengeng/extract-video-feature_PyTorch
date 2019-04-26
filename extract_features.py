#-*- coding: utf-8 -*-
import os
import ipdb
import time
import argparse
import numpy as np
import pandas as pd
import cv2

import torch
import torch.nn
import torchvision.models as models
from torch.autograd import Variable 
import torch.cuda
import torchvision.transforms as transforms
from PIL import Image

os.environ['CUDA_HOME'] = '/usr/local/cuda'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

img_to_tensor = transforms.ToTensor()

def make_model():
    resmodel=models.resnet18(pretrained=True)
    resmodel.cuda()
    return resmodel

# classification
def inference(resmodel,imgpath):
    resmodel.eval()
    
    img=Image.open(imgpath)
    img=img.resize((224,224))
    tensor=img_to_tensor(img)
    
    tensor=tensor.resize_(1,3,224,224)
    tensor=tensor.cuda()
            
    result=resmodel(Variable(tensor))
    result_npy=result.data.cpu().numpy()
    max_index=np.argmax(result_npy[0])
    
    return max_index
    
# feature extraction 
def extract_feature(resmodel,imgpath):
    resmodel.fc=torch.nn.LeakyReLU(0.1)
    resmodel.eval()
    
    img=Image.open(imgpath)
    img=img.resize((224,224))
    tensor=img_to_tensor(img)
    
    tensor=tensor.resize_(1,3,224,224)
    tensor=tensor.cuda()
            
    result=resmodel(Variable(tensor))
    result_npy=result.data.cpu().numpy()
    
    return result_npy[0]

def main():
    model = make_model()
    video_frames_path = '../frames/'
    feats_path = '../features/resnet18_feats/'
    video_frames = sorted(os.listdir(video_frames_path))
    for video_frame in video_frames:
        videos_path = os.path.join(video_frames_path , video_frame , '/' )
        videos = sorted(os.listdir(videos_path))
        for video in videos:
            frame_count = 0
            feature_list = []

            frames_path =  os.path.join(videos_path , video , '/' )
            frames = sorted(os.listdir(frames_path)) # check the order!!!
            print frames

            for img in frames:
                imgpath = frames_path+img
                frame_feature = extract_feature(model, imgpath)
                feature_list.append(frame_feature)
                frame_count += 1

            video_feature = np.array(feature_list)
            print ('%s,%s'%(video,frame_count))

            save_path = os.path.join(feats_path, video , '.npy')
            np.save(save_path, video_feature)

if __name__=="__main__":
    main()
