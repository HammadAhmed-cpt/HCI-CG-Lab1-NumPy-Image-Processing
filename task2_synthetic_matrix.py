import numpy as np
import matplotlib.pyplot as plt

img_matrix = np.zeros((300, 400, 3), dtype=np.uint8)

mid_h, mid_w = 300 // 2, 400 // 2


img_matrix[:mid_h, :mid_w] = [255, 0, 0]

img_matrix[:mid_h, mid_w:] = [0, 255, 0]

img_matrix[mid_h:, :mid_w] = [0, 0, 255]

img_matrix[mid_h:, mid_w:] = [255, 255, 255]

print("--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C): {img_matrix.shape}")
print(f"Data Type:             {img_matrix.dtype}")
print(f"Total Elements:        {img_matrix.size:,} values")
print(f"Memory Footprint:      {img_matrix.nbytes:,} bytes ({img_matrix.nbytes / 1024:.2f} KB)")

plt.imshow(img_matrix)
plt.title("Synthetic 4-Quadrant Matrix")
plt.axis("off")
plt.show()