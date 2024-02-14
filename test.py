import flet as ft


def example():
    def handle_change(e: ft.ControlEvent):
        print(f"change on panel with index {e.data}")

    panel = ft.ExpansionPanelList(
        elevation=8,
        on_change=handle_change,
        # controls=[
        #     # ft.ExpansionPanel(
        #     #     # has no header and content - placeholders will be used
        #     #     # bgcolor=ft.colors.BLUE_400,
        #     #     header=None,
        #     #     expanded=True,
        #     )
        # ],
    )

    for i in range(2):
        exp = ft.ExpansionPanel(
        )
        exp.header = ft.ListTile(
            title=ft.Text('hehehe')
        )
        exp.content = ft.ListTile(
            title=ft.Text(f"This is in Panel {i}"),
            subtitle=ft.Text(f"Press the icon to delete panel {i}"),
            trailing=ft.IconButton(ft.icons.DELETE)
        )

        panel.controls.append(exp)

    return panel


# import tasks as tsk
#
# loaded_tasks = tsk.load_tasks()
#
#
# def create_task_objesct(task_dict: dict):
#     one_l_task = tsk.Task(
#         task_id=task_dict['task_id'],
#         task_name=task_dict['task_name'],
#         task_description=task_dict['task_description'],
#         task_subtasks=task_dict['task_subtasks']
#     )
#     return one_l_task

"""


"""

