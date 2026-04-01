# Object Detection API

A Flask web application that detects objects in uploaded images using TensorFlow and a pre-trained model.

## Features
- Web interface for uploading images
- Real-time object detection using TensorFlow
- REST API endpoint for programmatic access
- Supports JPG, PNG, JPEG, and GIF formats

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the web UI:**
   Open `http://localhost:5000/detection-api` in your browser

## Project Structure
- `app.py` - Flask application and routes
- `image_object_detection.py` - TensorFlow detection logic
- `models/` - Pre-trained model files
- `object_detection_twitter/` - Label map and annotations
- `image-uploads/` - Uploaded images directory
- `templates/index.html` - Web interface

## API Endpoint
- **POST** `/detection-api` - Upload image and get detection results

## Dependencies
- Flask
- TensorFlow 1.15
- Pillow
- NumPy
- Matplotlib