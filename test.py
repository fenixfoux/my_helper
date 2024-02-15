import flet as ft
from flet import *
import tasks as tsk
ttsk = [
        {
            "task_id": 6,
            "task_name": "Task 2",
            "task_description": "Description 2",
            "task_subtasks": []
        },
        {
            "task_id": 29423,
            "task_name": "kkk",
            "task_description": "kkk 2",
            "task_subtasks": []
        },
        {
            "task_id": 349110,
            "task_name": "kkk",
            "task_description": "kkk 2",
            "task_subtasks": []
        },
        {
            "task_id": 195893,
            "task_name": "kkk",
            "task_description": "kkk 2",
            "task_subtasks": []
        },
        {
            "task_id": 126419,
            "task_name": "kkk",
            "task_description": "kkk 2",
            "task_subtasks": []
        },
        {
            "task_id": 612430,
            "task_name": "Kupite kenguru",
            "task_description": "kenguru required",
            "task_subtasks": []
        }]

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
def create_one_loaded_task_ui(one_task:dict):
    pass

def create_panel_with_loaded_task(all_loaded_tasks: dict):
    panel = ft.ExpansionPanelList()
    print(type(all_loaded_tasks))

    # for task in all_loaded_tasks['all_tasks']:
    #     print('-')
    # for task in all_loaded_tasks['all_tasks']:
    #     print(type(all_loaded_tasks[task]))

    # for i in all_loaded_tasks:
    #     print(f"type(i)------: {type(all_loaded_tasks[i])}")
    #     print(all_loaded_tasks[i])
    #     # create_one_loaded_task_ui()



    return panel


loaded_tasks = tsk.load_tasks()
create_panel_with_loaded_task(loaded_tasks)


# def main(page: Page):
#     # page.title = "Flet counter example"
#     # page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     test_page = example()
#     page.add(test_page)
#
# app(target=main)






#
# def create_task_objesct(task_dict: dict):
#     one_l_task = tsk.Task(
#         task_id=task_dict['task_id'],
#         task_name=task_dict['task_name'],
#         task_description=task_dict['task_description'],
#         task_subtasks=task_dict['task_subtasks']
#     )
#     return one_l_task

# def load_parse_tasks(tasks):
#     print(type(tasks))
#     for i in tasks:
#         print(tasks[i])
#         print(type(tasks[i]))
#
#
# load_parse_tasks(loaded_tasks)
"""


"""

