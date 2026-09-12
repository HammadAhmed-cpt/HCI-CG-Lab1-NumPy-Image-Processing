# Human-Computer Interaction (HCI) & Computer Graphics (CG)

**Course:** Introductory HCI & Computer Graphics  
**Department:** IMCS - Computer Science PE, University of Sindh  
**Instructor:** Sir Rajeesh  
**Student Name:** Hammad Ahmed  
**Roll / Seat Number:** 2k24/CSE/62  

---

## 📄 Submission Deliverables

* 📘 **[Lab 1 Report: Display Density Metrics & Image Array Mechanics in NumPy (PDF)](Hammad_Assginment_2.pdf)**
* 📗 **[Mini Assignment: Deconstructing HCI & Computer Graphics in Daily Software (PDF)](Hammad_Assginment_GoogleEarth.pdf)**

---

## 🛠️ Lab 1 Implementations

| Script | Functionality | Key Topics Covered |
| :--- | :--- | :--- |
| `task1_dpi_calculator.py` | Display Pixel Density (PPI/DPI) Calculator | Euclidean diagonal calculation, aspect ratio reduction via GCD, DPI classification (Low/Medium/High) |
| `task2_synthetic_matrix.py` | Synthetic Image Matrix Creation | 4-quadrant 300x400x3 RGB matrix (`uint8`), element count, memory footprint calculation |
| `task3_channel_slicing.py` | Channel Slicing & Isolation | 2D intensity grid extraction via Axis-2 slicing, zero-padded isolated RGB matrices, mean channel intensity analysis |
| `task4_downsampling.py` | Spatial Downsampling & Pixelation via Striding | Strided decimation (N=8), re-expansion via `np.repeat`, dimension and memory savings metrics |

---

## 💡 Theory Deliverable: RGBA vs. RGB Memory Footprint

**Question:** Why does adding an Alpha channel (RGBA) increase an image array's memory consumption by 33% compared to standard RGB?

**Answer:**  
An uncompressed 8-bit digital image array allocates 1 byte per color channel for every individual pixel (`np.uint8`):

* **Standard RGB:** Contains 3 channels per pixel (R, G, B), requiring:  
  `Memory_RGB = H * W * 3 * 1 byte`
* **RGBA:** Introduces a 4th channel (Alpha for transparency), requiring:  
  `Memory_RGBA = H * W * 4 * 1 byte`

The fractional increase in memory usage is:  
`(4 - 3) / 3 = 1 / 3 ≈ 33.33%`

Because array size scales linearly with the channel dimension along Axis 2, going from 3 channels to 4 channels directly adds exactly one-third (33.33%) to the total memory footprint.

---

## 🌐 Mini Assignment Summary: Google Earth Case Study

### 1. Human-Computer Interaction (HCI) Focus
* **Search Bar:** Prominent text field that acts as a primary navigation affordance, enabling direct search without manual pan/zoom navigation.
* **Dynamic Feedback Panel:** The Measure tool continuously displays live updates of length and heading to provide real-time feedback and reduce cognitive load.
* **Zoom Controls:** Simple, discoverable `+/-` buttons support direct manipulation over map scale, reinforcing recognition over recall.

### 2. Computer Graphics (CG) Focus
* **Directional Lighting & Cast Shadows:** Sunlight simulation casts consistent depth cues that make flat textures read as a 3D volume.
* **Photogrammetric 3D Mesh:** High-density surface geometry captures realistic, irregular building structures and rooftops from aerial imagery.
* **Photo-Based Texture Mapping:** Real photographs projected onto building surfaces provide realistic architectural detail without manual geometric modeling.

---

## 🚀 Running the Code

1. **Install requirements:**
   ```bash
   pip install numpy matplotlib pillow
