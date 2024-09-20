# widgets.py
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class ScoreLabel(Label):
    """
    自定义控件，用于显示分数
    """
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(ScoreLabel, self).__init__(**kwargs)
        self.text = f"Score: {self.score}"

    def update_score(self, new_score):
        """
        更新分数显示
        """
        self.score = new_score
        self.text = f"Score: {self.score}"
