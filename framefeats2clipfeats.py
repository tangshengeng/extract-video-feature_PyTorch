#-*- coding: utf-8 -*-
import os
import ipdb
import time
import argparse
import numpy as np
import pandas as pd
import math
import torch
import torch.nn as nn
from torch.autograd import Variable
import skimage.io as io
from skimage.transform import resize
from glob import glob
import json

os.environ['CUDA_HOME'] = '/usr/local/cuda'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

def main():
    input_folder = './features/resnet18_feats/'
    output_folder = './features/resnet18_clip_feats/'

    num = 1
    sum = len(os.listdir(input_folder))
    for video in sorted(os.listdir(input_folder)): 
        print 'video: ' + str(num) + '/'+ str(sum)
        num += 1
        # ipdb.set_trace()
        input_path = os.path.join(input_folder,video)
        output_path = os.path.join(output_folder,video)

        current_data = np.load(input_path)
        video_data = []

        for start, end in zip(range(0, len(current_data)-8, 4), range(8, len(current_data), 4)):
            batch_data = current_data[start:end]
            video_data.append(batch_data)

        video_data = np.array(video_data)
        np.save(output_path, video_data)

if __name__ == "__main__":
   main()

