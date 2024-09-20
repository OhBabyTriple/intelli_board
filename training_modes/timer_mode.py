# timer_mode.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from common.screen_base import BaseScreen

class TimerModeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(TimerModeScreen, self).__init__(**kwargs)
        self.time_left = 60  # 60秒倒计时
        self.score = 0       # 进球数
        layout = BoxLayout(orientation='vertical')

        # 显示倒计时
        self.timer_label = Label(text="Time: 60", font_size='40sp')
        layout.add_widget(self.timer_label)

        # 显示进球数
        self.score_label = Label(text="Score: 0", font_size='40sp')
        layout.add_widget(self.score_label)

        self.add_widget(layout)

        # 定时器，每秒减少一次倒计时
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.text = f"Time: {self.time_left}"

        if self.time_left == 0:
            Clock.unschedule(self.update_timer)  # 停止倒计时
            self.show_leaderboard()

    def on_key_press(self, key):
        """
        模拟进球，之后可以替换为传感器的进球检测
        """
        if key == 'space':  # 空格键表示进球
            self.score += 1
            self.score_label.text = f"Score: {self.score}"

    def show_leaderboard(self):
        # 切换到排行榜界面
        self.manager.current = 'leaderboard'