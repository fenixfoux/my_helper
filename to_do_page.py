import flet as ft
import tasks as tsk


class TodoTaskPage(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.page_title = 'Todo page'
        self.task_name_hint = 'Task name'
        self.task_description_hint = 'Task description'
        self.save_button_text = 'save'
        self.new_task_name = None
        self.new_task_description = None
        self.new_task_date_complete = None
        self.all_loaded_tasks = None

    def build(self):
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

    def create_task_section(self) -> ft.Column:
        self.new_task_name = ft.TextField(hint_text=self.task_name_hint)
        self.new_task_description = ft.TextField(hint_text=self.task_description_hint)
        save_task_button = ft.ElevatedButton(text=self.save_button_text, on_click=self.save_task)
        load_tasks_button = ft.ElevatedButton(text="load_tasks", on_click=self.load_all_tasks)

        created_task_section = ft.Column(
            controls=[
                self.new_task_name,
                self.new_task_description,
                save_task_button,
                load_tasks_button,
            ]
        )
        return created_task_section

    def save_task(self, e):
        if self.new_task_name.value:
            new_task_name = self.new_task_name.value
            new_task_description = self.new_task_description.value
            self.clear_creation_task_fields()
            print(new_task_name, new_task_description)
        else:
            print(f"task name can't be empty")

    # def create_ui_one_loaded_task(self):

    def load_all_tasks(self, e):
        loaded_tasks = tsk.load_tasks()
        print(loaded_tasks)

    def clear_creation_task_fields(self):
        self.new_task_name.value = ''
        self.new_task_description.value = ''
        self.new_task_name.update()
        self.new_task_description.update()

    def task_tabs_section(self):
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


def create_to_do_page_content():
    tst = TodoTaskPage()
    return tst
