import argparse
import cv2
import numpy as np
import os
import sys
import requests
import json
import torchvision
import torch 
import time


path='/home/ipx/python/taming-transformers-master/vqgan_data/train_data'
data=os.listdir('/home/ipx/python/taming-transformers-master/vqgan_data/train_data')

f = 'output.txt'
f = open(f, 'w')


for i in range(0,len(data),1):
	f.write('/home/ipx/python/taming-transformers-master/vqgan_data/train_data/'+data[i]+'\n')

f.close()