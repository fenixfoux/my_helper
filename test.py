import json
import os

import flet as ft
from flet import *
import all_variables as all_vars
import tasks as tsk


class TodoTaskPageUI(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.created_page = None
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
        self.modal_dialog_to_edit_task = ft.AlertDialog(title=ft.Text('asda'))

    def create_test_section(self) -> ft.Column:
        tt_text = ft.Text('Some text')
        return ft.Column(
            controls=[
                tt_text,
                ft.IconButton(
                    icons.ADD,
                    on_click=lambda e:self.rise_alert_dialog(e, tt_text.value)
                )
            ]
        )

    def rise_alert_dialog(self,e,some_text: str):
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes"),# on_click=close_dlg),
                ft.TextButton("No")#, on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def example(self):
        dlg = ft.AlertDialog(
            title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
        )

        def close_dlg(e):
            dlg_modal.open = False
            e.control.page.update()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=close_dlg),
                ft.TextButton("No", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        def open_dlg(e):
            e.control.page.dialog = dlg
            dlg.open = True
            e.control.page.update()

        def open_dlg_modal(e):
            e.control.page.dialog = dlg_modal
            dlg_modal.open = True
            e.control.page.update()

        return ft.Column(
            [
                ft.ElevatedButton("Open dialog", on_click=open_dlg),
                ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
            ]
        )

    def create_todo_task_page(self):
        self.created_page = ft.Column(controls=[
            self.create_test_section(),
            # self.modal_dialog_to_edit_task,
            self.example()
        ])

        return self.created_page

# ===== TESTING ===== #
def main(page: Page):
    # check_storage_file()
    todo_tp = TodoTaskPageUI()
    page.add(todo_tp.create_todo_task_page())


ft.app(target=main)