import flet as ft
from flet import *


class TodoTaskPageUI(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.some_value = ""
        self.tab_pages = ['all', 'active', 'completed']
        self.all_tasks = [{'task_name': 'default task name','task_description': 'default task description'},] # список словарей с задачами



    def create_new_task_section(self):
        # функция которая должна создавать UI с двумя полями для ввода текста и двумя кнопками, сохранить задачу и очистить поля
        pass

    def create_tabs_section(self):
        # функция которая должна создать UI в форме табов, количество вкладок соответствует элементам списка self.tab_pages
        pass

    def save_new_task(self):
        # функция сохранения новой задачи в общий список всех задач, эта функция должна срабатывать при нажатии на кнопку сохранить
        # так же при сохранении новой задачи должна будет вызываться функция update_tasks которая будет обновлять UI
        pass

    def update_tasks(self):
        # функция заполнения одного Tab-а в Tabs, эта функция должна смотреть в self.all_tasks и для каждого task создать текстовое поле в котором выведет данные
        pass

    def create_todo_task_page(self):
        return ft.Column()


# ===== TESTING ===== #
def main(page: Page):
    todo_tp = TodoTaskPageUI()
    page.add(todo_tp.create_todo_task_page())

ft.app(target=main)