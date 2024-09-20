# training_screen.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from common.screen_base import BaseScreen

class TrainingScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(TrainingScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # 按钮：选择计时模式
        timer_mode_button = Button(text="Timer Mode", size_hint=(0.5, 0.5))
        timer_mode_button.bind(on_press=self.start_timer_mode)

        # 按钮：选择计球模式
        score_mode_button = Button(text="Score Mode", size_hint=(0.5, 0.5))
        score_mode_button.bind(on_press=self.start_score_mode)

        score_mode_button = Button(text="Leaderboard", size_hint=(0.5, 0.5))
        score_mode_button.bind(on_press=self.start_leaderboard)

        layout.add_widget(Label(text="Select Training Mode", font_size='30sp'))
        layout.add_widget(timer_mode_button)
        layout.add_widget(score_mode_button)

        self.add_widget(layout)

    def start_timer_mode(self, instance):
        # 切换到计时模式界面
        self.manager.current = 'Timer Mode'

    def start_score_mode(self, instance):
        # 切换到计球模式界面
        self.manager.current = 'Score Mode'

    def start_leaderboard(self, instance):
        # 切换到计球模式界面
        self.manager.current = 'Leaderboard'
