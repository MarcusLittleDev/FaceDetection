import cv2
import numpy as np
import base64

# detects faces and returns image string


def detect_face(image):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # remove the data:image part
    encoded_data = image.split(',')[1]

    # convert string of image data to uint8
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)

    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    _, img_encoded = cv2.imencode('.jpg', img)

    imgString = base64.b64encode(img_encoded)

    return imgString.decode()
