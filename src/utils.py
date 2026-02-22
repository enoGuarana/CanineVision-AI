import cv2
import numpy as np

def load_video(path, max_frames=100):
    """Carrega vídeo e retorna frames"""
    cap = cv2.VideoCapture(path)
    frames = []
    count = 0
    
    while count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224, 224))
        frames.append(frame)
        count += 1
    
    cap.release()
    return np.array(frames)

def preprocess_frames(frames):
    """Normaliza frames para o modelo"""
    frames = frames.astype(np.float32) / 255.0
    return frames
