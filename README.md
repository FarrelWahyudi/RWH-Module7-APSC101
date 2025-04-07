# Topography Analyser with Elevation and Distance Mapping

## 📌 Overview
This Python GUI application allows users to:
- Load a topographic map image (with a visible colorbar)
- Select a base point and multiple target points interactively
- Calculate:
  - Distance between points
  - x and y displacement (in meters)
  - Elevation at each point (based on RGB mapping)
  - Elevation difference relative to the base point
- Display output as a table and plot directional arrows between points

Originally based on an image distance calculator by an unknown author. Modified and enhanced by **Farrel**, a UBC Computer Engineering student, to include elevation mapping, vector visualization, and data export.

---

## ⚙️ Requirements
- Python 3.x
- `Pillow`
- `Tkinter` (usually included with Python)
- `matplotlib`
- `pandas`

Install dependencies via pip if needed:
```bash
pip install pillow matplotlib pandas
```

---

## 🚀 How to Use

### 1. Run the Script
```bash
python tryAnalyzeTopography.py
```

### 2. Load a Map
Click the **"Select Image"** button and choose a topographic image (preferably one with an elevation color bar).

### 3. Select Points
- Click once to set the **base point** (shown in red).
- Click again to add **target points** (shown in blue).
- You can add as many as you like.

### 4. Calculate Results
- Click **"Calculate Distance & Elevation"**.
- The program will print a table in the console with:
  - Distance
  - Δx, Δy
  - Elevation
  - Elevation difference

### 5. Clear Points (Optional)
Click **"Clear Dots"** to reset point selection.

---

## 🧪 Sample Input / Output

### Input:
- Image: <img src="https://github.com/FarrelWahyudi/RWH-Module7-APSC101/blob/main/map-pointed.png?raw=true">
- Selected 32 Target Points

### Console Output:
```plaintext
Distance: 11.40 m | Δx: 11 m | Δy: -3 m | Elevation: 5 m | Elevation Δ: 5 m
Distance: 15.13 m | Δx: -15 m | Δy: 2 m | Elevation: 0 m | Elevation Δ: 0 m
Distance: 15.81 m | Δx: 5 m | Δy: -15 m | Elevation: 5 m | Elevation Δ: 5 m
Distance: 17.20 m | Δx: 14 m | Δy: 10 m | Elevation: 10 m | Elevation Δ: 10 m
Distance: 20.62 m | Δx: 5 m | Δy: 20 m | Elevation: 5 m | Elevation Δ: 5 m
Distance: 21.84 m | Δx: -6 m | Δy: -21 m | Elevation: 5 m | Elevation Δ: 5 m
Distance: 23.85 m | Δx: -13 m | Δy: 20 m | Elevation: -2.5 m | Elevation Δ: -2.5 m
Distance: 27.46 m | Δx: -23 m | Δy: -15 m | Elevation: 10 m | Elevation Δ: 10 m
Distance: 29.83 m | Δx: 19 m | Δy: -23 m | Elevation: 22.5 m | Elevation Δ: 22.5 m
Distance: 32.57 m | Δx: 31 m | Δy: -10 m | Elevation: -2.5 m | Elevation Δ: -2.5 m
Distance: 35.47 m | Δx: -13 m | Δy: -33 m | Elevation: 20 m | Elevation Δ: 20 m
Distance: 38.08 m | Δx: 9 m | Δy: 37 m | Elevation: 0 m | Elevation Δ: 0 m
Distance: 38.08 m | Δx: 35 m | Δy: 15 m | Elevation: 5 m | Elevation Δ: 5 m
Distance: 39.56 m | Δx: -14 m | Δy: 37 m | Elevation: -7.5 m | Elevation Δ: -7.5 m
Distance: 41.00 m | Δx: -41 m | Δy: 0 m | Elevation: 20 m | Elevation Δ: 20 m
Distance: 41.04 m | Δx: 28 m | Δy: -30 m | Elevation: 22.5 m | Elevation Δ: 22.5 m
Distance: 41.19 m | Δx: 4 m | Δy: -41 m | Elevation: 15 m | Elevation Δ: 15 m
Distance: 42.94 m | Δx: -20 m | Δy: -38 m | Elevation: 22.5 m | Elevation Δ: 22.5 m
Distance: 43.93 m | Δx: 29 m | Δy: 33 m | Elevation: 0 m | Elevation Δ: 0 m
Distance: 46.04 m | Δx: -38 m | Δy: -26 m | Elevation: 20 m | Elevation Δ: 20 m
Distance: 46.04 m | Δx: 46 m | Δy: 2 m | Elevation: 15 m | Elevation Δ: 15 m
Distance: 47.41 m | Δx: -42 m | Δy: 22 m | Elevation: 20 m | Elevation Δ: 20 m
Distance: 48.41 m | Δx: 38 m | Δy: -30 m | Elevation: -2.5 m | Elevation Δ: -2.5 m
Distance: 51.48 m | Δx: -7 m | Δy: 51 m | Elevation: -2.5 m | Elevation Δ: -2.5 m
Distance: 51.66 m | Δx: -38 m | Δy: 35 m | Elevation: 5 m | Elevation Δ: 5 m
Distance: 52.15 m | Δx: 44 m | Δy: -28 m | Elevation: 0 m | Elevation Δ: 0 m
Distance: 52.77 m | Δx: 47 m | Δy: 24 m | Elevation: 22.5 m | Elevation Δ: 22.5 m
Distance: 55.46 m | Δx: 24 m | Δy: 50 m | Elevation: 10 m | Elevation Δ: 10 m
Distance: 59.46 m | Δx: -44 m | Δy: -40 m | Elevation: 15 m | Elevation Δ: 15 m
Distance: 61.85 m | Δx: -35 m | Δy: 51 m | Elevation: 10 m | Elevation Δ: 10 m
Distance: 63.25 m | Δx: 40 m | Δy: -49 m | Elevation: -7.5 m | Elevation Δ: -7.5 m
Distance: 68.62 m | Δx: 47 m | Δy: 50 m | Elevation: 22.5 m | Elevation Δ: 22.5 m
Reference Elevation at base point: 0 m
DONE
```

---

## 🧾 Credits
- Original Code Author: Muhammad Nabil Alhanif
- Modified and expanded by: **Farrel Aryo Wahyudi**

---

## 📂 Future Improvements
- Export table to CSV/Excel
- Auto-detect colorbar scale
- 3D surface plots from elevation data
- Zoom & pan support in GUI

---

## 📬 Contact
Feel free to reach out for collaboration or feedback:
**Farrel Aryo Wahyudi**
Undergraduate Student at UBC Applied Science (Engineering)
 
Email: fwahyudi@student.ubc.ca
Phone: +1 (604) 830 5454

Happy mapping! 🌍🚀

