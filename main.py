import os
import shutil
from tkinter import Tk, filedialog
import cv2
import numpy as np
import mediapipe as mp
import threading

def select_folder():
    """Open a file dialog to select a folder."""
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory()
    return folder_path

def move_to_tmp_folder(image_path, tmp_folder):
    """Move the image to the tmp folder."""
    if not os.path.exists(tmp_folder):
        os.makedirs(tmp_folder)
    shutil.move(image_path, tmp_folder)

def is_single_person_visible(image_path):
    """Determine if an image contains a single clearly visible person using Mediapipe."""
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)

    if results.detections and len(results.detections) == 1:
        # One face detected
        return True
    else:
        # No face or more than one face detected
        return False

def process_image(image_path, tmp_folder):
    """Process a single image to check for a single clearly visible person."""
    if not is_single_person_visible(image_path):
        move_to_tmp_folder(image_path, tmp_folder)
        print(f"Moved {os.path.basename(image_path)} to tmp folder.")
    else:
        print(f"{os.path.basename(image_path)} contains a single clearly visible person.")

def main():
    folder_path = select_folder()
    if not folder_path:
        print("No folder selected. Exiting...")
        return

    tmp_folder = os.path.join(folder_path, "tmp")
    threads = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            thread = threading.Thread(target=process_image, args=(image_path, tmp_folder))
            thread.start()
            threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Processing complete.")

if __name__ == "__main__":
    main()
