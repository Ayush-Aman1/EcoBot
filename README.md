# EcoBot
A YOLOv11 based trash detection and greedy best first search model for trash detection and route optimisation for cleaning via a bot (on water surface) 

## Features

-  **YOLOv11** for object detection (Ultralytics)
-  **Depth Anything v2** for pixel-wise depth estimation
-  **3D coordinate estimation** of trash using bounding box and depth map
-  **Greedy Best-First Search (GBFS)** for target prioritization
-  Real-time webcam feed with annotated detections
-  Output video & JSON logging of coordinates (`trash_coords.json`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Ayush-Aman1/EcoBot.git
   cd EcoBot
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download model weights (will be downloaded automatically on first run)

## Usage

Run the main script:

```bash
python run.py
```

## Acknowledgments

- YOLOv11 by Ultralytics
- Depth Anything v2 by Microsoft 
