#!/usr/bin/env python3
import os
import torch

from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

cxx_args = ["-std=c++11"]

nvcc_args = [
    "-gencode",
    "arch=compute_30,code=sm_30",
    "-gencode",
    "arch=compute_35,code=sm_35",
    "-gencode",
    "arch=compute_37,code=sm_37",
    "-gencode",
    "arch=compute_50,code=sm_50",
    "-gencode",
    "arch=compute_52,code=sm_52",
    "-gencode",
    "arch=compute_60,code=sm_60",
    "-gencode",
    "arch=compute_61,code=sm_61",
    '-gencode', 'arch=compute_70,code=sm_70',
    '-gencode', 'arch=compute_70,code=compute_70',
    '-gencode', 'arch=compute_75,code=compute_75',
    "-gencode", "arch=compute_75,code=sm_75"
]

setup(
    name="filterinterpolation_cuda",
    ext_modules=[
        CUDAExtension(
            "filterinterpolation_cuda",
            ["filterinterpolation_cuda.cc", "filterinterpolation_cuda_kernel.cu"],
            extra_compile_args={"cxx": cxx_args, "nvcc": nvcc_args},
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
