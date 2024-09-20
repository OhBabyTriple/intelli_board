# screen_base.py

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.selected_button_index = 0  # 当前选择的按钮索引
        self.buttons = []  # 存储所有按钮
        self.feedback_label = Label(text="", font_size='20sp', color=(1, 1, 1, 0))  # 提示文本

    def update_button_selection(self):
        """
        更新按钮的背景颜色，以表示当前选中的按钮
        """
        for index, button in enumerate(self.buttons):
            if index == self.selected_button_index:
                button.background_color = (0, 1, 0, 1)  # 绿色表示选中
            else:
                button.background_color = (1, 1, 1, 1)  # 白色表示未选中

    def select_next_button(self):
        """
        选择下一个按钮
        """
        self.selected_button_index = (self.selected_button_index + 1) % len(self.buttons)
        self.update_button_selection()
        self.show_feedback("Next button selected!")

    def select_previous_button(self):
        """
        选择前一个按钮
        """
        self.selected_button_index = (self.selected_button_index - 1) % len(self.buttons)
        self.update_button_selection()
        self.show_feedback("Previous button selected!")


    def confirm_selection(self):
        # 确认选择当前的按钮
        current_button = self.buttons[self.selected_button_index]
        self.manager.current = current_button.text
        self.show_feedback("Selection confirmed!")



    def show_feedback(self, message):
        """
        显示手势识别反馈的提示信息和按钮颜色的变化
        """
        current_button = self.buttons[self.selected_button_index]
        current_button.background_color = (0, 0, 1, 1)  # 蓝色表示手势识别

        # 显示反馈提示文字
        self.feedback_label.text = message
        self.feedback_label.color = (1, 1, 1, 1)  # 白色显示

        # 定时器：1秒后恢复按钮颜色和提示文本的透明度
        Clock.schedule_once(self.reset_feedback, 1)

    def reset_feedback(self, dt):
        """
        恢复按钮颜色和提示文本状态
        """
        self.update_button_selection()
        self.feedback_label.text = ""
        self.feedback_label.color = (1, 1, 1, 0)  # 隐藏文字
