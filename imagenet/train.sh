export CUDA_VISIBLE_DEVICES=0,1
#export CUDA_VISIBLE_DEVICES=1

python main.py -a resnet18 --dist-url 'tcp://127.0.0.1:23457' --dist-backend 'nccl' --multiprocessing-distributed --world-size=1 --rank 0 --batch-size=512 --workers 4 /paddle/work/github/PyTorch/examples/imagenet
