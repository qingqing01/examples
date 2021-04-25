import torch
from decode_jpeg import decode_jpeg_cuda, read_file
import cv2

m = cv2.imread('/paddle/data/ImageNet/train/n13133613/ILSVRC2012_val_00019877.JPEG')
print(m.shape)
print(cv2.imread('/paddle/data/ImageNet/train/n02177972/ILSVRC2012_val_00033035.JPEG').shape)
im = read_file('/paddle/data/ImageNet/train/n02177972/ILSVRC2012_val_00033035.JPEG')
im = decode_jpeg_cuda(im, 3)
print(im)
