import cv2
from gestures.hand_tracking import HandTracking


def main():
    cap = cv2.VideoCapture(0)  # 打开主机的摄像头
    hand_tracking = HandTracking()

    while True:
        success, frame = cap.read()
        if not success:
            break

        # 识别手势
        gesture = hand_tracking.detect_gesture(frame)

        if gesture:
            print(f"Detected Gesture: {gesture}")

        # 显示摄像头画面
        cv2.imshow('Hand Tracking', frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    hand_tracking.release()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
