import json

import flet as ft
import tasks as tsk
from flet import *
import os
from all_variables import storage_file_path


def check_storage_file():
    if not os.path.exists(storage_file_path):
        with open(storage_file_path, "w", encoding='utf-8') as new_file:
            json.dump({"all_tasks": [
                {
                    "task_id": 1,
                    "task_name": "default task name",
                    "task_description": "default description",
                    "task_subtasks": []
                }
            ]}, new_file, indent=4)


def create_one_task_card_ui(one_task: dict) -> ft.Card:
    task_control_buttons = ft.Row(
        alignment=MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Row(
                spacing=0,
                controls=[
                    ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
                    ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
                    ft.IconButton(icons.HIGHLIGHT_REMOVE),
                ],
            ),
            ft.Row(
                spacing=0,
                controls=[
                    ft.IconButton(icons.ADD),
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
            ],
        )))
    return one_task_card


class TodoTaskPage(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.page_title = ''
        self.task_name_hint = 'Task name'
        self.task_description_hint = 'Task description'
        self.save_button_text = 'save'
        self.new_task_name = None
        self.new_task_description = None
        self.new_task_date_complete = None
        self.all_loaded_tasks = tsk.load_tasks()
        # self.main_tabs_wrapper = ft.Column()
        self.main_tab_wrapper = self.create_main_tasks_list_ui()


    def build(self):
        check_storage_file()
        page_title = ft.Text(value=self.page_title, )
        created_task_section = self.create_task_section()
        created_tasks_tab_section = self.task_tabs_section()

        page_content = ft.Column(
            controls=[
                page_title,
                created_task_section,
                created_tasks_tab_section,
            ]
        )
        return page_content

    def create_main_tasks_list_ui(self) -> ft.Column:
        """take a list of all tasks and create UI for each task without subtasks, add in Column controls and return
        its"""
        main_wrapper = ft.Column(
            scroll=ScrollMode.AUTO
        )
        for task in self.all_loaded_tasks['all_tasks']:
            one_card = create_one_task_card_ui(task)
            main_wrapper.controls.append(one_card)
        return main_wrapper

    def task_tabs_section(self):
        return ft.Tabs(
            selected_index=0,
            animation_duration=300,
            # width=400,
            height=400,
            tabs=[
                ft.Tab(
                    text="Main tasks",
                    content=self.main_tab_wrapper
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.SEARCH),
                    content=ft.Text("This is Tab 2"),
                ),
                ft.Tab(
                    text="Tab 3",
                    icon=ft.icons.SETTINGS,
                    content=ft.Text("This is Tab 3"),
                ),
            ],
        )

    def create_task_section(self) -> ft.Column:
        """UI section to collect data for new task and save it"""
        self.new_task_name = ft.TextField(hint_text=self.task_name_hint)
        self.new_task_description = ft.TextField(hint_text=self.task_description_hint)
        save_task_button = ft.ElevatedButton(text=self.save_button_text, on_click=self.save_task)
        clear_task_fields = ft.ElevatedButton(text="clear", on_click=self.clear_creation_task_fields)
        test_add_field_button = ft.ElevatedButton(text="add ui", on_click=self.test_add_fields)

        created_task_section = ft.Column(
            controls=[
                self.new_task_name,
                self.new_task_description,
                ft.Row([save_task_button, clear_task_fields, test_add_field_button])
            ]
        )
        return created_task_section

    def save_task(self, e):
        self.all_loaded_tasks = tsk.load_tasks()
        if self.new_task_name.value:
            new_task_name = self.new_task_name.value
            new_task_description = self.new_task_description.value
            self.clear_creation_task_fields(e)
            print(new_task_name, new_task_description)
            tsk.task_crud(
                self.all_loaded_tasks,
                new_task_name,
                new_task_description,
                None,
                operation_type='adding'
            )
            self.all_loaded_tasks = tsk.load_tasks()  # update all tasks list
            print(self.all_loaded_tasks)
            self.main_tab_wrapper = self.create_main_tasks_list_ui()
            self.update()
        else:
            print(f"task name can't be empty")

    def clear_creation_task_fields(self, e):
        self.new_task_name.value = ''
        self.new_task_description.value = ''
        self.new_task_name.update()
        self.new_task_description.update()

    def test_add_fields(self, e):
        print('button test_add_field_button was clicked')


def create_to_do_page_content(one_page):
    check_storage_file()
    todo_page = TodoTaskPage()
    created_task_section = todo_page.create_task_section()
    created_tab_section = todo_page.task_tabs_section()
    return Column(
        controls=[
            TextButton('go home', on_click=lambda _: one_page.go('/')),
            Column(
                controls=[
                    created_task_section,
                    created_tab_section,
                    Text(value="================="),
                ]),
            TextButton('go home2', on_click=lambda _: one_page.go('/')),
            Text(value="Second Page"),
            Text(value="Second Page"),
            Text(value="Second Page"),
        ],
    )


# # ===== TESTING ===== #
# def main(page: Page):
#     page.add(create_to_do_page_content(View))
#
# ft.app(target=main)