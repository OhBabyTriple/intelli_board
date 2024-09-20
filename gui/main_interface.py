import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from common.screen_base import BaseScreen
from gestures.hand_tracking import HandTracking  # 导入手势识别模块
from training_modes.traning_screen import TrainingScreen
from training_modes.score_mode import ScoreModeScreen
from training_modes.timer_mode import TimerModeScreen
from training_modes.leaderboard import LeaderboardScreen

class MainMenu(BaseScreen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.selected_button_index = 0  # 当前选择的按钮索引
        self.buttons = []  # 存储所有按钮
        self.feedback_label = Label(text="", font_size='20sp', color=(1, 1, 1, 0))  # 提示文本

        layout = BoxLayout(orientation='vertical')

        # 添加菜单按钮
        start_training_button = Button(text="Training Mode", size_hint=(0.5, 0.5))


        # 绑定鼠标点击事件
        start_training_button.bind(on_press=self.start_training)


        layout.add_widget(Label(text="Smart Basketball Backboard", font_size='30sp'))
        layout.add_widget(start_training_button)
        layout.add_widget(self.feedback_label)  # 添加反馈提示到布局中

        # 将按钮存储在列表中
        self.buttons = [start_training_button]
        self.add_widget(layout)

    def start_training(self, instance):
        # 切换到计时模式界面
        self.manager.current = 'Training Mode'



    def go_back(self, instance):
        # 返回主菜单
        self.manager.current = 'menu'


# 主应用程序类，集成手势识别和 GUI
class SmartBackboardApp(App):
    def __init__(self, **kwargs):
        super(SmartBackboardApp, self).__init__(**kwargs)
        # 只在应用启动时打开摄像头
        self.cap = cv2.VideoCapture(0)

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainMenu(name='menu'))
        self.sm.add_widget(TrainingScreen(name='Training Mode'))
        self.sm.add_widget(ScoreModeScreen(name='Score Mode'))
        self.sm.add_widget(TimerModeScreen(name='Timer Mode'))
        self.sm.add_widget(LeaderboardScreen(name='Leaderboard'))


        # 创建手势识别对象
        self.hand_tracker = HandTracking()

        # 启动手势检测的定时器
        Clock.schedule_interval(self.update_hand_tracking, 1.0 / 10.0)  # 每 1/10 秒更新一次

        return self.sm

    def update_hand_tracking(self, dt):
        """
        每帧更新手势识别并根据手势控制界面
        """
        frame = self.capture_frame()
        gesture = self.hand_tracker.detect_gesture(frame)

        if gesture == 'point_1':
            self.sm.current_screen.select_previous_button()  # 选择前一个按钮
        elif gesture == 'point_2':
            self.sm.current_screen.select_next_button()  # 选择下一个按钮
        elif gesture == 'ok':
            self.sm.current_screen.confirm_selection()  # 确认选择
        elif gesture == 'open_hand':
            self.stop()  # 退出程序

    def capture_frame(self):
        """
        模拟摄像头捕捉帧的功能
        """
        ret, frame = self.cap.read()  # 通过 OpenCV 捕捉视频帧
        return frame

    def on_stop(self):
        """
        当应用退出时关闭摄像头
        """
        if self.cap.isOpened():
            self.cap.release()  # 释放摄像头


if __name__ == '__main__':
    SmartBackboardApp().run()
