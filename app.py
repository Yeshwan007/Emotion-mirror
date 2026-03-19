import cv2
from face_module.face_detect import detect_face_emotion
from text_module.text_detect import detect_text_emotion
from fusion_module.fusion import fuse_emotions

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_emotion = detect_face_emotion(frame)

    text = input("Enter text: ")
    text_emotion = detect_text_emotion(text)

    final_emotion = fuse_emotions(face_emotion, text_emotion)

    print("Face:", face_emotion)
    print("Text:", text_emotion)
    print("Final:", final_emotion)

    cv2.imshow("Emotion Mirror", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()