import os

# 项目根目录
project_name = "E:\Code\pycharm\intelli_board"

# 模块列表及其文件结构
modules = {
    "gestures": ["hand_tracking.py", "gesture_model.py"],
    "scoring": ["score_tracker.py", "score_statistics.py"],
    "gui": ["main_interface.py", "animations.py", "widgets.py"],
    "training_modes": ["mode_selection.py", "virtual_competition.py"],
    "reminders": ["goal_setting.py", "reminder_service.py"],
    "data_management": ["data_store.py", "data_query.py"],
}


# 创建项目结构
def create_project_structure(project_name, modules):
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        print(f"Created project directory: {project_name}")

    for module, files in modules.items():
        module_path = os.path.join(project_name, module)
        if not os.path.exists(module_path):
            os.mkdir(module_path)
            print(f"Created module directory: {module_path}")

        for file in files:
            file_path = os.path.join(module_path, file)
            with open(file_path, 'w') as f:
                f.write(f"# {file}\n")
            print(f"Created file: {file_path}")

    # 创建主入口文件
    main_file_path = os.path.join(project_name, "main.py")
    with open(main_file_path, 'w') as f:
        f.write("# Main entry point of the smart backboard project\n")
    print(f"Created file: {main_file_path}")


# 执行创建项目结构
create_project_structure(project_name, modules)
