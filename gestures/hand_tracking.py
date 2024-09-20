import cv2
import mediapipe as mp
import math


class HandTracking:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gesture(self, image):
        """
        识别手势
        :param image: 摄像头捕捉的帧
        :return: 手势字符串 ('fist', 'open_hand', 'point_1', 'point_2', 'ok') 或 None
        """
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = self.hands.process(image_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                # 检测手势
                if self.is_ok_sign(hand_landmarks):
                    return 'ok'
                elif self.is_pointing_2(hand_landmarks):
                    return 'point_2'
                elif self.is_pointing_1(hand_landmarks):
                    return 'point_1'
                elif self.is_fist(hand_landmarks):
                    return 'fist'
                elif self.is_open_hand(hand_landmarks):
                    return 'open_hand'

        return None

    def calculate_angle(self, a, b, c):
        """
        计算三个点之间的夹角（用于判断手指关节的角度）
        :param a: 第一个点
        :param b: 第二个点（关节）
        :param c: 第三个点
        :return: 夹角
        """
        angle = math.degrees(math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x))
        return abs(angle)% 360

    def is_finger_bent(self, landmarks, mcp, pip):
        """
        判断手指是否弯曲，计算 MCP 和 PIP 关节的两个角度之和
        :param landmarks: 手部关键点
        :param mcp: MCP关节
        :param pip: PIP关节
        :return: True 如果两个角度和小于 180 度, 否则为 False
        """
        # 计算 MCP 的角度
        angle_mcp = self.calculate_angle(landmarks.landmark[mcp - 1], landmarks.landmark[mcp], landmarks.landmark[pip])

        # 计算 PIP 的角度
        angle_pip = self.calculate_angle(landmarks.landmark[mcp], landmarks.landmark[pip], landmarks.landmark[pip + 1])

        # 如果两个角度之和小于 180 度，认为手指是弯曲的
        if (angle_mcp + angle_pip) < 180:
            return True
        return False

    def is_fist(self, landmarks):
        """
        判断是否为拳头手势：所有手指弯曲
        """
        for finger in [self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
                       self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                       self.mp_hands.HandLandmark.RING_FINGER_MCP,
                       self.mp_hands.HandLandmark.PINKY_MCP]:
            if not self.is_finger_bent(landmarks, finger, finger + 1):
                return False
        return True

    def is_open_hand(self, landmarks):
        """
        判断是否为伸展五指手势：所有手指伸展
        """
        for finger in [self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
                       self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                       self.mp_hands.HandLandmark.RING_FINGER_MCP,
                       self.mp_hands.HandLandmark.PINKY_MCP]:
            if self.is_finger_bent(landmarks, finger, finger + 1):
                return False  # 只要有一根手指弯曲，则返回 False
        return True

    def is_pointing_1(self, landmarks):
        """
        判断是否为比1手势：食指伸展，其他手指弯曲
        """
        # 食指是否伸展
        if self.is_finger_bent(landmarks,
                               self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
                               self.mp_hands.HandLandmark.INDEX_FINGER_PIP):
            return False  # 食指弯曲则不符合

        # 检查其他手指是否弯曲
        for finger in [self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                       self.mp_hands.HandLandmark.RING_FINGER_MCP,
                       self.mp_hands.HandLandmark.PINKY_MCP]:
            if not self.is_finger_bent(landmarks, finger, finger + 1):
                return False  # 其他手指未弯曲则不符合
        return True

    def is_pointing_2(self, landmarks):
        """
        判断是否为比2手势：食指和中指伸展，其他手指弯曲
        """
        # 食指是否伸展
        if self.is_finger_bent(landmarks,
                               self.mp_hands.HandLandmark.INDEX_FINGER_MCP,
                               self.mp_hands.HandLandmark.INDEX_FINGER_PIP):
            return False  # 食指弯曲则不符合

        # 中指是否伸展
        if self.is_finger_bent(landmarks,
                               self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                               self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP):
            return False  # 中指弯曲则不符合

        # 检查无名指和小指是否弯曲
        for finger in [self.mp_hands.HandLandmark.RING_FINGER_MCP,
                       self.mp_hands.HandLandmark.PINKY_MCP]:
            if not self.is_finger_bent(landmarks, finger, finger + 1):
                return False  # 无名指或小指未弯曲则不符合
        return True

    def is_ok_sign(self, landmarks):
        """
        判断是否为OK手势：大拇指和食指形成圈，其他手指伸展
        """
        thumb_tip = landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        index_finger_tip = landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]

        # 计算大拇指和食指尖端之间的距离
        distance = math.sqrt((thumb_tip.x - index_finger_tip.x) ** 2 + (thumb_tip.y - index_finger_tip.y) ** 2)

        # 判断大拇指和食指是否靠近形成圈
        if distance < 0.05:  # 当它们距离足够近时，认为形成了圈
            # 检查其他手指是否伸展
            for finger in [self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP,
                           self.mp_hands.HandLandmark.RING_FINGER_MCP,
                           self.mp_hands.HandLandmark.PINKY_MCP]:
                if self.is_finger_bent(landmarks, finger, finger + 1):
                    return False  # 如果其他手指弯曲，返回 False
            return True
        return False

    def release(self):
        """
        释放资源
        """
        self.hands.close()
