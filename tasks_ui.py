import flet as ft
from flet import *
import tasks as tsk


class TaskUI(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.new_task_name = None
        self.new_task_description = None
        self.new_task_date_complete = None
        self.all_loaded_tasks = None

    def block_creation_new_task(self):
        self.new_task_name = ft.TextField(label="Task name", hint_text="Please enter the task name")
        self.new_task_description = ft.TextField(label="Task description",
                                                 hint_text="Please enter the task description")
        new_task_add_button = ft.ElevatedButton(text="Submit", on_click=self.add_button_clicked)
        load_tasks_button = ft.ElevatedButton(text="load_tasks", on_click=self.load_all_tasks)

        return ft.Column(controls=[self.new_task_name, self.new_task_description, new_task_add_button, load_tasks_button])

    def add_button_clicked(self, e):
        if self.new_task_name.value:
            new_task_name = self.new_task_name.value
            new_task_description = self.new_task_description.value
            self.clear_creation_task_fields()
            print(new_task_name, new_task_description)
        else:
            print(f"task name can't be empty")


    def clear_creation_task_fields(self):
        self.new_task_name.value = ''
        self.new_task_description.value = ''
        self.new_task_name.update()
        self.new_task_description.update()

    def load_all_tasks(self, e):
        loaded_tasks = tsk.load_tasks()  # Call the load_tasks function to load tasks from the file
        print(loaded_tasks)

    def block_of_task_tabs(self):
        return ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.Container(
                        content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                    ),
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
            width=400,
            height=400,
        )


def main(page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.update()
    task_ui = TaskUI()
    page.add(
        task_ui.block_creation_new_task(),
        task_ui.block_of_task_tabs()
    )


ft.app(target=main)
