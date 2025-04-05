from ultralytics import YOLO
import cv2

# Emotion weights
emotion_scores = {
    'Boredom': 3, 
    'Confusion': 3, 
    'Engaged': 5, 
    'Frustration': 2, 
    'Sleepy': 0,
    'Yawning': 0
}

# Prediction function
def predict(chosen_model, img, classes=[], conf=0.5):
    if classes:
        results = chosen_model.predict(img, classes=classes, conf=conf)
    else:
        results = chosen_model.predict(img, conf=conf)
    return results

# Load the model
model = YOLO("train/weights/best.pt")

# Read the image
image = cv2.imread("2.jpg")

# Get predictions
results = predict(model, image, classes=[], conf=0.5)

# Calculate the score
total_score = 0
detected_classes = []

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]
        detected_classes.append(class_name)
        if class_name in emotion_scores:
            total_score += emotion_scores[class_name]
   

print("\nDetected Emotions:", detected_classes)
print("Total Score:", total_score)
