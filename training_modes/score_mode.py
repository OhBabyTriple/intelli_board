# score_mode.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from common.screen_base import BaseScreen
import time

class ScoreModeScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(ScoreModeScreen, self).__init__(**kwargs)
        self.target_score = 10  # 用户选择的目标进球数
        self.current_score = 0  # 当前进球数
        self.start_time = time.time()  # 计时开始时间

        layout = BoxLayout(orientation='vertical')

        # 显示当前进球数和目标
        self.score_label = Label(text=f"Score: {self.current_score}/{self.target_score}", font_size='40sp')
        layout.add_widget(self.score_label)

        # 显示计时
        self.time_label = Label(text="Time: 0", font_size='40sp')
        layout.add_widget(self.time_label)

        self.add_widget(layout)

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        elapsed_time = int(time.time() - self.start_time)
        self.time_label.text = f"Time: {elapsed_time}"

        if self.current_score >= self.target_score:
            Clock.unschedule(self.update_time)
            self.show_leaderboard()

    def on_key_press(self, key):
        """
        模拟进球，之后可以替换为传感器的进球检测
        """
        if key == 'space':  # 空格键表示进球
            self.current_score += 1
            self.score_label.text = f"Score: {self.current_score}/{self.target_score}"

    def show_leaderboard(self):
        # 切换到排行榜界面
        self.manager.current = 'leaderboard'
