def fuse_emotions(face_emotion, text_emotion):
    if face_emotion == text_emotion:
        return face_emotion
    else:
        return f"{face_emotion} / {text_emotion}"