from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension, CUDAExtension
image_link_flags=['nvjpeg']
includes = [' /usr/local/cuda-10.1/include/']
setup(name='decode_jpeg',
      ext_modules=[CUDAExtension('decode_jpeg', ['decode_jpeg_cuda.cc'], include_dirs=includes,libraries=image_link_flags),],
      cmdclass={'build_ext': BuildExtension})
