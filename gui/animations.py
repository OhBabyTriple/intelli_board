# animations.py
from kivy.animation import Animation
from kivy.uix.button import Button

def animate_button(button: Button):
    """
    对按钮添加动画效果
    """
    # 创建一个动画，将按钮逐渐放大
    anim = Animation(size_hint=(0.6, 0.6), duration=0.5)
    # 将按钮缩小回原来的大小
    anim += Animation(size_hint=(0.5, 0.5), duration=0.5)
    # 开始动画
    anim.start(button)
