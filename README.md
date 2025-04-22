📷 Face Recognition Attendance System
This project uses OpenCV and DeepFace to mark attendance by detecting and recognizing faces from a live webcam feed. When the spacebar is pressed, a photo is captured and matched against a database of known faces.

🛠 Features
Live webcam capture

Face detection and recognition using DeepFace

Automatic image saving and comparison

Attendance marking based on face match

Uses RetinaFace + FaceNet backend for accuracy


📁 Directory Structure

`├── attendance_library/       # Folder with reference images (known students)`
`├── captured_pics/            # Temporary folder for captured webcam images`
`├── face_detection.py         # Main script`
🚀 How It Works
Launches the webcam using OpenCV

Press Space to take a picture, or Esc to exit

Captured image is compared with stored images in attendance_library/

If a match is found:

Attendance is marked

Image is displayed with confirmation

If no match is found:

Attendance is not marked

Notification is displayed on image

🧠 Tech Stack
Python 3.8+

OpenCV for webcam and image processing

DeepFace for face recognition

Backend: Facenet

Detector: RetinaFace

📦 Installation

# Clone the repository
`git clone https://github.com/aakarshank/Attendance-App.git`

# Create a virtual environment (optional but recommended)
<pre><code>```python -m venv venv
.\venv\Scripts\activate```</code></pre>

# Install dependencies
`pip install opencv-python deepface`

Make sure to place clear, front-facing images in the attendance_library/ directory.
File names are not used — only facial features are compared.

▶️ Usage
<pre><code>```python face_detection.py```</code></pre>


⚠️ Notes
For better accuracy, use high-quality reference images.

enforce_detection=False allows processing even if the face is not clearly detected (use with caution).
