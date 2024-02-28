import json
import os

import flet as ft
from flet import *
import all_variables as all_vars
import tasks as tsk


class TodoTaskPageUI(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.some_value = ""
        self.page_name = all_vars.page_name_eng
        self.tab_page_names = all_vars.all_tab_names_eng
        self.check_storage_file = tsk.check_storage_file()
        self.all_tasks = tsk.load_tasks()  # список словарей с задачами
        self.all_existed_keys = []
        # self.all_tasks = all_vars.default_list_of_tasks  # список словарей с задачами
        # self.new_tasks_section_controls = self.create_new_task_section()

        self.new_task_name_field = None
        self.new_task_description_field = None
        self.all_tabs = None

    def create_new_task_section(self):
        self.new_task_name_field = TextField(hint_text=all_vars.new_task_name_hint_eng)
        self.new_task_description_field = ft.TextField(hint_text=all_vars.new_task_description_hint_eng)
        return ft.Column([
            ft.Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(self.page_name),
                    ft.ElevatedButton(all_vars.button_back_text_eng)
                ]),
            self.new_task_name_field,
            self.new_task_description_field,
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text=all_vars.save_new_task_button_text_eng,
                        on_click=lambda e: self.save_new_task(
                            e,
                            self.new_task_name_field.value,
                            self.new_task_description_field.value,
                            None,
                            'adding'
                        )

                    ),
                    ft.ElevatedButton(
                        text=all_vars.clear_fields_new_task_button_text_eng,
                        on_click=self.clear_new_task_section_fields),
                    ft.ElevatedButton(all_vars.test_button_text_eng),
                ]
            )
        ])
        # функция которая должна создавать UI с двумя полями для ввода текста и двумя кнопками, сохранить задачу и
        # очистить поля

    def clear_new_task_section_fields(self, e):
        self.new_task_name_field.value = ''
        self.new_task_description_field.value = ''
        self.new_task_name_field.update()
        self.new_task_description_field.update()
        # todo: find a way to clean and update all fields all immediately not one by one

    def create_one_task_card_ui(self, one_task: dict) -> ft.Card:
        task_id_field = ft.Text(
            value=one_task['task_id'],
            visible=False
        )
        task_id = task_id_field.value
        task_control_buttons = ft.Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
                        ft.IconButton(
                            icons.HIGHLIGHT_REMOVE,
                            on_click=lambda e: self.test_press_get_value(e, task_id),
                            data=task_id),
                    ],
                ),
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(  # edit current task
                            icons.EDIT,
                            on_click=lambda e: self.edit_current_task(e,)
                        ),
                        ft.IconButton(  # add a subtask
                            icons.ADD,
                            # on_click=lambda e: self.save_new_task(e, 'lll', 'imper', task_id)
                        ),
                        ft.IconButton(icons.START),
                        ft.IconButton(icons.STAR),
                    ],
                )
            ]
        )

        task_info = ft.ListTile(
            title=ft.Text(one_task['task_name']),
            subtitle=ft.Text(
                value=one_task['task_description'],
                italic=True
            )
        )
        one_task_card = ft.Card(
            content=ft.Container(ft.Column(
                spacing=0,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                wrap=False,
                controls=[
                    task_control_buttons,
                    task_info,
                    task_id_field
                ],
            )))
        return one_task_card

    def create_tabs_section(self):
        # функция которая должна создать UI в форме табов, количество вкладок соответствует элементам списка
        # self.tab_pages
        self.all_tabs = ft.Tabs(height=400, )
        for one_tab_name in self.tab_page_names:
            self.all_tabs.tabs.append(
                self.load_tasks(tab_name=one_tab_name)
            )
        return self.all_tabs

    def save_new_task(self, e, new_task_name, new_task_description, parent_id=None, operation_type=''):
        # функция сохранения новой задачи в общий список всех задач, эта функция должна срабатывать при нажатии на
        # кнопку сохранить так же при сохранении новой задачи должна будет вызываться функция update_tasks которая
        # будет обновлять UI
        if new_task_name.strip():
            generated_unique_id = tsk.generate_unique_task_id(self.all_existed_keys)
            tsk.task_crud(
                main_list_tasks=self.all_tasks,
                task_id=generated_unique_id,
                task_name=new_task_name,
                task_description=new_task_description,
                parent_task_id=parent_id,
                operation_type=operation_type
            )
            self.all_tasks = tsk.load_tasks()  # update list of all tasks
            # update UI by appending created new task if this is not a subtask
            if parent_id is None:
                created_task = tsk.find_task_by_id(self.all_tasks['all_tasks'], generated_unique_id)
                for tab in self.all_tabs.tabs:
                    if tab.text == 'all':
                        tab_content = tab.content
                        # print(type(tab_content))
                        if isinstance(tab_content, ft.Column):
                            tab_content.controls.append(self.create_one_task_card_ui(created_task))
                            self.all_tabs.update()
                            break
            # update all existed keys
            self.all_existed_keys = tsk.get_all_existing_keys(self.all_tasks['all_tasks'], self.all_existed_keys)
            self.clear_new_task_section_fields(e)

    def edit_current_task(self,e):
        """open modal dialog with inputs filled with task's data and allow to modify and save the task"""
        print(f"status: the function is not implemented yet"
              f"purpose: open modal dialog with inputs filled with task's data and allow to modify and save the task")
        pass

    def load_tasks(self, tab_name):
        # функция заполнения одного Tab-а в Tabs, эта функция должна смотреть в self.all_tasks и для каждого task
        # создать текстовое поле в котором выведет данные
        # return pg
        tab_wrapper = ft.Column(scroll=ScrollMode.AUTO)
        if tab_name == 'all':
            for one_task in self.all_tasks['all_tasks']:
                tab_wrapper.controls.append(self.create_one_task_card_ui(one_task))
        return ft.Tab(
            text=tab_name,
            content=tab_wrapper
        )

    def create_todo_task_page(self):
        created_page = ft.Column(controls=[
            self.create_new_task_section(),
            self.create_tabs_section(),
        ])

        return created_page

    def test_press_get_value(self, e, task_id):
        print('icon button was pressed')
        print(f"type of 'e': {type(e)}")
        print(f"task id of this card is: {task_id}")


# ===== TESTING ===== #
def main(page: Page):
    # check_storage_file()
    todo_tp = TodoTaskPageUI()
    page.add(todo_tp.create_todo_task_page())


ft.app(target=main)
