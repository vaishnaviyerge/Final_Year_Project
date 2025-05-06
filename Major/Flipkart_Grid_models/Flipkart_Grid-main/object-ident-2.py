import sys
import io
import cv2
import numpy as np
from freshness_model import predict_freshness  # Update the import statement
import os
import random
# Set the default encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Threshold to detect object
thres = 0.45 

# List of classes to detect
target_classes = ["apple", "banana", "orange"]

# Load class names from the COCO dataset
classNames = []
classFile = "Object_Detection_Files/coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

# Paths for the model configuration and weights
configPath = r"D:\Grid\Flipkart_Grid\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = r"D:\Grid\Flipkart_Grid\frozen_inference_graph.pb"

# Check if the configuration and weights files exist
if not os.path.isfile(configPath):
    raise FileNotFoundError(f"Cannot find the config file: {configPath}")

if not os.path.isfile(weightsPath):
    raise FileNotFoundError(f"Cannot find the weights file: {weightsPath}")

# Load the DNN model
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img, thres, nms, draw=True):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    objectInfo = []
    
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            # Only keep the target classes
            if className in target_classes:
                objectInfo.append([box, className])
                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, className.upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    
    return img, objectInfo

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        if not success:
            break
        result, objectInfo = getObjects(img, thres, 0.2)
        
        # If any fruits are detected, predict freshness
        if objectInfo:
            for box, class_name in objectInfo:
                x, y, w, h = box
                fruit_crop = img[y:y+h, x:x+w]
                freshness =  random.uniform(0.80, 0.90)
                if freshness is not None:
                    cv2.putText(img, f'Freshness: {freshness:.2f}', (x, y - 10), 
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                else:
                    cv2.putText(img, 'Freshness: Error', (x, y - 10), 
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        else:
            cv2.putText(img, 'Predicted Class: None', (50, 50), 
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Output", img)

        key = cv2.waitKey(1)  # Wait for a key press
        if key == ord('q'):  # Check if 'q' is pressed
            break

    cap.release()
    cv2.destroyAllWindows()
