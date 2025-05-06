# Final_Year_Project - https://github.com/vaishnaviyerge/Final_Year_Project/tree/master
Quality &amp; Quantity analyser : Btech - Final Year Project

Objective - Design a smart quality test system utilizing camera vision technology for India’s 
leading ecommerce company. The system should be able to assess the shipment quality 
and quantity  effectively and efficiently.

1] open cv 
OpenCV (Open Source Computer Vision Library) is an open-source library mainly used for real-time computer vision and image processing tasks. It supports operations like object detection, image filtering, face recognition, and more using Python, C++, and Java.


2] OCR
OCR (Optical Character Recognition) is a technology that converts different types of text images—such as scanned documents, photos of signs, or handwritten notes—into machine-readable text. It’s commonly used to digitize printed documents for editing, searching, and storage.

3]  YOLO
YOLO (You Only Look Once) is a real-time object detection algorithm that identifies and localizes multiple objects in a single pass through a neural network. It divides an image into grids and predicts bounding boxes and class probabilities for objects directly, making it extremely fast and efficient.

4] CNN 
CNN (Convolutional Neural Network) is a type of deep learning model designed for processing and analyzing visual data like images. It uses convolutional layers to automatically detect patterns such as edges, textures, and shapes, making it highly effective for image classification, object detection, and recognition tasks.


Quality Detection Steps -

OVERALL FLOW:
User uploads product image → frontend sends it to backend → backend uses a model to predict quality → result (confidence score) is returned and shown on frontend.

BACKEND (Python + Django + TensorFlow + OpenCV + CNN)
1. User uploads image from frontend
When the user selects or uploads an image, it is sent via an API call to Django backend (POST /fresh_detect/ endpoint).

This endpoint is mapped in urls.py to views.py.

2. views.py handles the image
In views.py (inside freshness_detector app), code uses:

python
Copy
Edit
import tensorflow as tf
import cv2
The image is:

Read (using cv2.imread() or Django's InMemoryUploadedFile).

Preprocessed (resized, normalized).

Converted to a tensor (for feeding into the model).

3. CNN Model loads + predicts
Pre-trained CNN model (saved as .h5 or .pb) is loaded with:

python
Copy
Edit
model = tf.keras.models.load_model('path_to_model')
The image tensor is passed through the model:

python
Copy
Edit
prediction = model.predict(processed_image)
Output: a confidence score (e.g., 0.91) indicating the freshness/quality level.

4. Backend sends prediction
Django returns a JSON response like:

json
Copy
Edit
{
  "freshness_score": 0.918
}

FRONTEND (HTML + JS + AJAX or Fetch API)
1. HTML Upload UI
A simple form lets user upload an image.

JavaScript grabs the image and sends it via fetch() or XMLHttpRequest.

2. JavaScript handles response
Once the API responds with confidence_score, JS:

Updates the UI to show score.

Optionally displays a bar chart (Freshness vs Confidence Score) using Chart.js or similar.

3. Display uploaded image
Image preview is shown using:

js
Copy
Edit
document.getElementById('preview').src = URL.createObjectURL(image)
Example: How Quality Detection Works
Upload "banana.png"

JavaScript sends it to /fresh_detect/

Django reads it → preprocesses it → feeds it into TensorFlow CNN model

Model predicts: 91.8% fresh

Response: { "freshness_score": 0.918 }

UI updates: “Product Quality Score: 91.8%”

Quantity Detection - 

Project Flow: Quantity Prediction
User uploads image ➝ image sent to backend ➝ YOLO model detects objects ➝ returns count ➝ frontend displays quantity count & visual highlights

BACKEND (Django + YOLO + OpenCV)
1. User Uploads Image
A POST request is made to the backend Django view from the frontend.

Django view receives the uploaded image (e.g., apples, bananas, etc.).

2. Backend Receives Image
The view (views.py) retrieves the uploaded file from request.FILES.

python
Copy
Edit
image = request.FILES['image']

3. Read Image using OpenCV
The image is converted to OpenCV format:

python
Copy
Edit
img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)

4. Load YOLOv5 / YOLOv8 Model
Pre-trained YOLO model is loaded:

python
Copy
Edit
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

5. Perform Detection
Model runs detection on the image:

python
Copy
Edit
results = model(img)

6. Extract Quantity Info
Get total detected objects or classes of interest:

python
Copy
Edit
quantity = len(results.xyxy[0])  # number of detected objects
Optionally, object class names and bounding boxes are retrieved too.

7. Annotate Image with Boxes (Optional)
Bounding boxes are drawn using OpenCV or results.save() to visualize predictions.

8. Return Response
JSON response:

json
Copy
Edit
{
  "quantity": 3,
  "detected_items": ["apple", "apple", "apple"]
}
Or return image with boxes to show prediction visually.

FRONTEND (HTML + JavaScript)
1. Image Upload UI
User selects an image to predict quantity.

JavaScript captures the image.

2. Send to Backend
JavaScript uses fetch() or axios:

js
Copy
Edit
fetch('/quantity_predict/', {
  method: 'POST',
  body: formData,
})

3. Handle Response
Once the quantity is returned, JS updates:

Quantity count (Detected: 3 apples)

Optionally displays annotated image with bounding boxes.

4. Display Result
UI shows:

Number of items detected

Labeled image (optional)

Chart like Quantity vs Type (optional with Chart.js)

Real Example:
Upload image with 4 bananas.

Image sent to backend → YOLO model runs.

Model detects 4 objects.

Response: { "quantity": 4 }

UI updates: “Detected Quantity: 4”

Text recognition process

Text Detection and Recognition (OCR)
Goal: Detect and extract printed or handwritten text (like expiry date, batch no, brand name) from product images.

BACKEND (Django + OpenCV + Tesseract OCR)
1. Image Uploaded by User
The frontend sends the image file to the backend via POST request.

python
Copy
Edit
image = request.FILES['image']

2. Image Preprocessing (Optional but Important)
Convert image to OpenCV format:

python
Copy
Edit
img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
Convert to grayscale:

python
Copy
Edit
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Apply thresholding or denoising to enhance text:

python
Copy
Edit
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

3. Text Detection with Tesseract OCR
Use pytesseract (Python wrapper for Google Tesseract OCR):

python
Copy
Edit
import pytesseract
text = pytesseract.image_to_string(thresh)
You can also get bounding boxes:

python
Copy
Edit
boxes = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)

4. Return Extracted Text
The recognized text is returned as JSON:

json
Copy
Edit
{
  "extracted_text": "Fresh Banana\nExpiry: 25 May 2025\nBatch: A123"
}
Optional: send annotated image with text regions highlighted.

FRONTEND (HTML + JS)
1. UI for Uploading Image
The user uploads a product image (containing printed text).

JavaScript prepares and sends the image using fetch() or axios.

2. Handle Backend Response
After the backend returns the extracted text:

js
Copy
Edit
.then(response => response.json())
.then(data => {
   document.getElementById("ocrResult").innerText = data.extracted_text;
});

3. Display in UI
Show the detected text in a text area, or alongside the image.

Sample Flow Summary

Step	Action
1.	Upload image of product
2.	Image → Django backend
3.	OpenCV → Grayscale/Threshold
4.	Tesseract OCR extracts text
5.	Return text to frontend
6.	Display text on screen

Tech Used:
OpenCV: Image preprocessing.

Tesseract OCR: Text extraction.

pytesseract: Python integration of Tesseract.

Django: Server-side handling.

JS/HTML: Frontend display.







