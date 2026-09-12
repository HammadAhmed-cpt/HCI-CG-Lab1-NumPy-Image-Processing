# Human-Computer Interaction (HCI) & Computer Graphics (CG)

**Course:** Introductory HCI & Computer Graphics[cite: 4]
**Department:** IMCS - Computer Science PE, University of Sindh[cite: 4]  
**Instructor:** Sir Rajeesh[cite: 4]  
**Student Name:** Hammad Ahmed[cite: 3, 4]  
**Roll / Seat Number:** 2k24/CSE/62[cite: 3, 4]  

---

## 📄 Submission Deliverables

* 📘 **[Lab 1 Report: Display Density Metrics & Image Array Mechanics in NumPy (PDF)](Hammad_Assginment.pdf)**[cite: 3]
* 📗 **[Mini Assignment: Deconstructing HCI & Computer Graphics in Daily Software (PDF)](Hammad_Assginment_GoogleEarth.pdf)**[cite: 4]

---

## 🛠️ Lab 1 Implementations

| Script | Functionality | Key Topics Covered |
| :--- | :--- | :--- |
| `task1_dpi_calculator.py` | Display Pixel Density (PPI/DPI) Calculator[cite: 3] | Euclidean diagonal calculation, aspect ratio reduction via GCD, DPI classification (Low/Medium/High)[cite: 3] |
| `task2_synthetic_matrix.py` | Synthetic Image Matrix Creation[cite: 3] | 4-quadrant $300 \times 400 \times 3$ RGB matrix (`uint8`), element count, memory footprint calculation[cite: 3] |
| `task3_channel_slicing.py` | Channel Slicing & Isolation[cite: 3] | 2D intensity grid extraction via Axis-2 slicing, zero-padded isolated RGB matrices, mean channel intensity analysis[cite: 3] |
| `task4_downsampling.py` | Spatial Downsampling & Pixelation via Striding[cite: 3] | Strided decimation ($N=8$), re-expansion via `np.repeat`, dimension and memory savings metrics[cite: 3] |

---

## 💡 Theory Deliverable: RGBA vs. RGB Memory Footprint

**Question:** Why does adding an Alpha channel (RGBA) increase an image array's memory consumption by 33% compared to standard RGB?[cite: 3]

**Answer:**  
An uncompressed 8-bit digital image array allocates 1 byte per color channel for every individual pixel (`np.uint8`)[cite: 3]:

* **Standard RGB:** Contains 3 channels per pixel (R, G, B), requiring:[cite: 3]
  $$\text{Memory}_{\text{RGB}} = H \times W \times 3 \times 1\text{ byte}$$[cite: 3]
* **RGBA:** Introduces a 4th channel (Alpha for transparency), requiring:[cite: 3]
  $$\text{Memory}_{\text{RGBA}} = H \times W \times 4 \times 1\text{ byte}$$[cite: 3]

The fractional increase in memory usage is:[cite: 3]
$$\frac{\text{Memory}_{\text{RGBA}} - \text{Memory}_{\text{RGB}}}{\text{Memory}_{\text{RGB}}} = \frac{4 - 3}{3} = \frac{1}{3} \approx 33.33\%$$[cite: 3]

Because array size scales linearly with the channel dimension ($C$) along Axis 2, going from 3 channels to 4 channels directly adds exactly one-third (33.33%) to the total memory footprint[cite: 3].

---

## 🌐 Mini Assignment Summary: Google Earth Case Study

### 1. Human-Computer Interaction (HCI) Focus[cite: 4]
* **Search Bar:** Prominent text field that acts as a primary navigation affordance, enabling direct search without manual pan/zoom navigation[cite: 4].
* **Dynamic Feedback Panel:** The Measure tool continuously displays live updates of length and heading to provide real-time feedback and reduce cognitive load[cite: 4].
* **Zoom Controls:** Simple, discoverable `+/-` buttons support direct manipulation over map scale, reinforcing recognition over recall[cite: 4].

### 2. Computer Graphics (CG) Focus[cite: 4]
* **Directional Lighting & Cast Shadows:** Sunlight simulation casts consistent depth cues that make flat textures read as a 3D volume[cite: 4].
* **Photogrammetric 3D Mesh:** High-density surface geometry captures realistic, irregular building structures and rooftops from aerial imagery[cite: 4].
* **Photo-Based Texture Mapping:** Real photographs projected onto building surfaces provide realistic architectural detail without manual geometric modeling[cite: 4].

---

## 🚀 Running the Code

1. **Install requirements:**
   ```bash
   pip install numpy matplotlib pillow
