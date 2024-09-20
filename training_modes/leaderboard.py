# leaderboard.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from common.screen_base import BaseScreen

class LeaderboardScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(LeaderboardScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

    def on_enter(self):
        # 清除上次显示的内容
        self.layout.clear_widgets()

        # 模拟排行榜显示
        self.layout.add_widget(Label(text="Leaderboard", font_size='30sp'))
        self.layout.add_widget(Label(text="1. Player A - 50 points", font_size='20sp'))
        self.layout.add_widget(Label(text="2. Player B - 40 points", font_size='20sp'))
        self.layout.add_widget(Label(text="3. Player C - 35 points", font_size='20sp'))

        # 提示拍照
        self.layout.add_widget(Label(text="You are in the top 3! Please make an 'OK' gesture to take a photo."))
