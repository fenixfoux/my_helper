import flet as ft
import todo_code.auxiliary_functions as aux_f
from flet import *
from storage import all_variables as all_vars
from todo_code import tasks_refactored as tsk
from storage.all_variables import new_task_creation


class OneTaskPage(ft.UserControl):
    """
    universal UI to create page for one task. every task will have a button to open its page where will be displayed
    all info like short/long description, list of subtasks and subtasks of subtasks etc
    """

    def __init__(self, one_task: dict):
        super().__init__()
        self.created_page = None
        self.one_task = one_task
        self.subtask_name_text_size = 18
        self.subtask_description_text_size = 16

    def created_main_info_task_section(self) -> ft.Column:
        task_id = ft.Text(
            key='task_id',
            value=self.one_task['task_id'],
            visible=True
        )
        task_name = ft.Text(
            key='task_name',
            value=self.one_task['task_name'],
            size=20,
            weight=FontWeight.BOLD,
        )
        task_description = ft.Text(
            key='task_description',
            value=self.one_task['task_description'],
            disabled=True,
            size=16,
        )
        edit_button = ft.IconButton(
            icons.REBASE_EDIT,
            on_click=lambda e: self.task_operation_edit(
                e,
                task_id=task_id.value,
                task_name=task_name.value,
                task_description=task_description.value
            ),
            # on_click=lambda e: self.edit_task(e),
        )
        done_button = ft.IconButton(
            icons.DONE,
            on_click=lambda event: self.task_operation_done(event)
        )
        wrapper = ft.Row(
            controls=[
                ft.Column(
                    expand=9,
                    controls=[
                        task_id,
                        task_name,
                        task_description,
                    ]),
                ft.Column(
                    expand=1,
                    horizontal_alignment=CrossAxisAlignment.END,
                    controls=[
                        edit_button,
                        done_button,
                    ])
            ]
        )
        created_main_section = ft.Column(
            key='main_section',
            controls=[
                wrapper,
            ]
        )
        return created_main_section

    def task_operation_done(self, e):
        decision = aux_f.create_alert_dialog(e, "Mark task as Done?")
        print(f"received: {decision}")
        print(f"need to implement actions after mark task as done, also the logic to make changes in depend of "
              f"the current status")

    def task_operation_edit(self, e, task_id, task_name, task_description):
        # print(type(e.control.page.controls))
        temp_dict = {
            "task_id": task_id,
            "task_name": task_name,
            "task_description": task_description
        }
        decision, modified_dict = aux_f.modify_task_alert_dialog(e, "Modify task", temp_dict)
        # self.find_field_by_key(e, 'task_name', e.control.page.controls)
        print(decision)
        print(modified_dict)

    def find_field_by_key(self, e, key: str, controls):
        for field in controls:
            if field.key == key:
                print(f"Received key '{key}': found")
                print(field)
                field.value = 'krea krea'
                e.control.page.update()
                break
            try:
                if field.controls:
                    self.find_field_by_key(e, key, field.controls)
            except AttributeError:
                pass

    def created_second_info_task_section(self) -> ft.Column:
        created_second_section = ft.Column(
            key='second_section'
        )
        return created_second_section

    def create_one_task_page(self) -> ft.Column:
        """create content of one task page and return it"""
        self.created_page = ft.Column(
            controls=[
                self.created_main_info_task_section(),
                self.created_second_info_task_section(),

            ]
        )
        return self.created_page


# ===== TESTING ===== #
def main(page: Page):
    # check_storage_file()
    todo_tp = OneTaskPage(new_task_creation)
    page.add(todo_tp.create_one_task_page())


#
ft.app(target=main)
