import torch

print(torch.__version__)  # PyTorch version
print(torch.version.cuda)  # CUDA Version num
print(torch.cuda.is_available())  # True if CUDA is working/installed properly
print(torch.cuda.device_count())  # Num of avail GPUs
print(torch.cuda.get_device_name(0))  # GPU name


### OUTPUT
# 2.6.0+cu126
# 12.6
# True
# 1
# NVIDIA GeForce RTX 4060