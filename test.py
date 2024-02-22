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
        # one_task = create_one_task_ui()

        panel.controls.append(exp)

    return panel


def create_one_task_ui(one_task: dict) -> ft.ExpansionPanel:
    task_name = one_task['task_name']
    if len(one_task['task_description'].strip()) == 0:
        task_description = 'may be any subtasks can help ?'
    else:
        task_description = one_task['task_description']
    exp = ft.ExpansionPanel(
    )
    exp.header = ft.ListTile(
        title=ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            # leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text(f"{task_name}"),
                            subtitle=ft.Text(
                                f"{task_description}", italic=True
                            ),
                        ),
                        ft.Row(
                            # todo: find a way to align the buttons vertically equal to the task name for the buttons
                            #  below
                            [
                                ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
                                ft.IconButton(icons.HIGHLIGHT_REMOVE),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ],
                ),
                # width=400,
                # padding=10,
            )
        )
    )
    if len(one_task['task_subtasks']) != 0:
        print('subtasks')
        for subtask in one_task['task_subtasks']:
            create_one_task_ui(subtask)
            exp.content = create_one_task_ui(subtask)
    else:
        exp.content = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(' ')
                ]
            )
        )
    return exp


def create_panel_with_loaded_task(all_loaded_tasks: dict):
    panel = ft.ExpansionPanelList()
    print(type(all_loaded_tasks))
    for task in all_loaded_tasks['all_tasks']:
        created_task = create_one_task_ui(task)
        panel.controls.append(created_task)
    # for task in all_loaded_tasks['all_tasks']:
    #     print('-')
    # for task in all_loaded_tasks['all_tasks']:
    #     print(type(all_loaded_tasks[task]))

    # for i in all_loaded_tasks:
    #     print(f"type(i)------: {type(all_loaded_tasks[i])}")
    #     print(all_loaded_tasks[i])
    #     # create_one_loaded_task_ui()

    return panel


# loaded_tasks = tsk.load_tasks()
# create_panel_with_loaded_task(loaded_tasks)


def main(page: Page):
    # page.title = "Flet counter example"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # test_page = example()
    # page.add(test_page)

    loaded_tasks = tsk.load_tasks()
    test_panel = create_panel_with_loaded_task(loaded_tasks)
    page.add(test_panel)


app(target=main)
