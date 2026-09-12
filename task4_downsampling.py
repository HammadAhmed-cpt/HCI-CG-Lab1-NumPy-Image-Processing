import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Automatically resolve the correct path to sample.jpg
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'sample.jpg')

# 1. Load image and convert to NumPy array
raw_img = Image.open(image_path)
img = np.array(raw_img)

N = 8

# 2. Downsample using strided slicing along axis 0 and axis 1
downsampled = img[::N, ::N, :]

# 3. Re-expand using np.repeat across axes 0 and 1
pixelated = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)

# Crop re-expanded array to match exact dimensions if not cleanly divisible by N
pixelated = pixelated[:img.shape[0], :img.shape[1], :]

# 4. Memory & dimension reduction metrics
dim_reduction = (1 - (downsampled.shape[0] / img.shape[0])) * 100
mem_savings = (1 - (downsampled.nbytes / img.nbytes)) * 100

print(f"--- DOWNSAMPLING ANALYSIS (N={N}) ---")
print(f"Original Shape:      {img.shape} | Memory: {img.nbytes:,} bytes")
print(f"Downsampled Shape:   {downsampled.shape} | Memory: {downsampled.nbytes:,} bytes")
print(f"Re-expanded Shape:   {pixelated.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {dim_reduction:.2f}% reduction per axis")
print(f"Memory Savings:      {mem_savings:.2f}% data reduction")

# 5. Visual comparison
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img)
ax[0].set_title("Original Image")
ax[0].axis("off")

ax[1].imshow(pixelated)
ax[1].set_title(f"Pixelated (Downsampled N={N} & Re-expanded)")
ax[1].axis("off")

plt.tight_layout()
plt.show()