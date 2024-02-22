import flet as ft
from flet import *
import tasks as tsk


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

def create_main_tasks_list_ui(all_tasks: dict) -> ft.Column:
    """take a list of all tasks and create UI for each task without subtasks, add in Column controls and return its"""
    main_wrapper = ft.Column()
    for task in all_tasks['all_tasks']:
        one_card = create_one_task_card_ui(task)
        main_wrapper.controls.append(one_card)
    return main_wrapper

def main(page: Page):
    t_ui = create_main_tasks_list_ui(tsk.load_tasks())
    page.add(t_ui)
    # for i in range(3):
    #     page.add(create_one_task_card_ui())


app(target=main)
