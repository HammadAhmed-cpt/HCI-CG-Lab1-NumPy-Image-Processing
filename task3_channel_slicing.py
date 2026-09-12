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

# 2. Extract 2D intensity grids via Axis 2 slicing[cite: 1]
r_2d = img[:, :, 0]
g_2d = img[:, :, 1]
b_2d = img[:, :, 2]

# 3. Construct 3D single-channel isolation matrices[cite: 1]
red_only = np.zeros_like(img)
red_only[:, :, 0] = r_2d

green_only = np.zeros_like(img)
green_only[:, :, 1] = g_2d

blue_only = np.zeros_like(img)
blue_only[:, :, 2] = b_2d

# Print metrics summary[cite: 1]
print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape:   {img.shape}")
print(f"Red Channel 2D Shape:   {r_2d.shape} | Mean Intensity: {r_2d.mean():.2f}")
print(f"Green Channel 2D Shape: {g_2d.shape} | Mean Intensity: {g_2d.mean():.2f}")
print(f"Blue Channel 2D Shape:  {b_2d.shape} | Mean Intensity: {b_2d.mean():.2f}")

# 4. Render 2x3 Subplot Grid[cite: 1]
fig, axes = plt.subplots(2, 3, figsize=(12, 7))

# Top row: Color isolation[cite: 1]
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red Channel (Isolated)")
axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green Channel (Isolated)")
axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue Channel (Isolated)")

# Bottom row: Grayscale intensity maps[cite: 1]
axes[1, 0].imshow(r_2d, cmap='gray')
axes[1, 0].set_title("Red 2D Intensity")
axes[1, 1].imshow(g_2d, cmap='gray')
axes[1, 1].set_title("Green 2D Intensity")
axes[1, 2].imshow(b_2d, cmap='gray')
axes[1, 2].set_title("Blue 2D Intensity")

for ax in axes.ravel():
    ax.axis("off")

plt.tight_layout()
plt.show()