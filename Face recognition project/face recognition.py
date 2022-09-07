import cv2

print("Connecting to server...")

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

p_message = True
img_array = []

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    #prank message
    if p_message: 
        print("Creating 'Video_capture.mp4'...")
        if(x or y or w or h):
            cropped_image = img[y:y+h, x: x+w]
            cv2.imwrite("output/Cropped Image.jpg", cropped_image)

        p_message = False

    #create video
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

    # Display
    cv2.imshow('Camera capture  -  (esc to close)', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff

    if k==27:
        break
# Release the VideoCapture object
cap.release()

out = cv2.VideoWriter("face_output/Video_capture.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()