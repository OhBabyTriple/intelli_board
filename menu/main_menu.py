# main_menu.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from common.screen_base import BaseScreen  # 导入基类

class MainMenu(BaseScreen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # 添加菜单按钮
        start_training_button = Button(text="Start Training", size_hint=(0.5, 0.5))
        virtual_comp_button = Button(text="Virtual Competition", size_hint=(0.5, 0.5))

        # 绑定鼠标点击事件
        start_training_button.bind(on_press=self.start_training)
        virtual_comp_button.bind(on_press=self.start_virtual_competition)

        layout.add_widget(Label(text="Smart Basketball Backboard", font_size='30sp'))
        layout.add_widget(start_training_button)
        layout.add_widget(virtual_comp_button)
        layout.add_widget(self.feedback_label)  # 添加反馈提示到布局中

        # 将按钮存储在列表中
        self.buttons = [start_training_button, virtual_comp_button]
        self.update_button_selection()

        self.add_widget(layout)

    def start_training(self, instance):
        # 切换到训练模式界面
        self.manager.current = 'training'

    def start_virtual_competition(self, instance):
        # 切换到虚拟比赛界面
        self.manager.current = 'virtual_competition'
