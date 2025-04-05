# Create the README.md file with the provided content
readme_content = """
# 🧠 Engagement Detection using YOLOv11s

This project detects student engagement from webcam images using a custom-trained **YOLOv11s** model. It identifies different emotional states like `Engaged`, `Bored`, `Confused`, `Sleepy`, etc., and calculates a total score based on detections. The goal is to help educational tools track user attentiveness and adjust interactions in real time.

---

## 🎯 Features

- Real-time engagement detection using deep learning
- Custom-trained YOLOv11s model
- Emotion classification with scoring
- Easy-to-run Python script with OpenCV

---

## 📊 ENGAGEMENT Scoring

Each detected class contributes to a total score based on the following weightage:

```python
{
    'Boredom': 3,
    'Confusion': 3,
    'Engaged': 5,
    'Frustration': 2,
    'Sleepy': 0,
    'Yawning': 0
}
