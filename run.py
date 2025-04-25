import threading
import subprocess
import json
import time
import math

# === Function to launch detect_coord_store.py in background ===
def launch_detection():
    print("Launching detect_coord_store.py for detection...")
    subprocess.run(["python3", "detect_coord_store.py"])

# === Function to read trash coordinates ===
def read_trash_coords():
    try:
        with open("trash_coords.json", "r") as f:
            return json.load(f)
    except Exception:
        return []

# === Greedy Best First Search simulation ===
def get_nearest_trash(trash_coords, current_position):
    def heuristic(trash):
        x1, y1 = current_position
        x2, y2 = (trash["bbox"][0] + trash["bbox"][2]) // 2, (trash["bbox"][1] + trash["bbox"][3]) // 2
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if not trash_coords:
        return None
    return min(trash_coords, key=heuristic)

# === Main GBFS Control Loop ===
def control_loop():
    print("Starting GBFS control loop...")
    current_position = (640 // 2, 480 // 2)  # Assuming center of frame as origin

    while True:
        trash_coords = read_trash_coords()
        if trash_coords:
            target = get_nearest_trash(trash_coords, current_position)
            if target:
                center_x = (target["bbox"][0] + target["bbox"][2]) // 2
                center_y = (target["bbox"][1] + target["bbox"][3]) // 2
                depth = target["depth"]
                print(f"➡️  Target: {target['class']} at ({center_x}, {center_y}), depth: {depth:.2f}")
        else:
            print("⚠️  No trash detected.")

        time.sleep(0.5)

# === Run detection in a separate thread ===
detection_thread = threading.Thread(target=launch_detection, daemon=True)
detection_thread.start()

# === Start GBFS control ===
control_loop()
