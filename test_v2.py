import flet as ft
from flet import *
import tasks as tsk

dict_storage = {
    "all_tasks": [
        {
            "task_id": 1,
            "task_name": "Task 2",
            "task_description": "as",
            "task_subtasks": [
                {
                    "task_id": 2,
                    "task_name": "Task 2",
                    "task_description": "Description 2",
                    "task_subtasks": [
                        {
                            "task_id": 3,
                            "task_name": "Task 2",
                            "task_description": "Description 2",
                            "task_subtasks": []
                        },
                        {
                            "task_id": 4,
                            "task_name": "Task 2",
                            "task_description": "Description 2",
                            "task_subtasks": []
                        }
                    ]
                },
                {
                    "task_id": 5,
                    "task_name": "Task 2",
                    "task_description": "Description 2",
                    "task_subtasks": []
                }
            ]
        },
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
        }
    ]
}


def create_one_task_ui(one_task: dict):
    task_padding = 5
    ret_exp = ft.ExpansionTile()
    # ret_exp.title = ft.Text('-'+'\n'+one_task['task_name'], padding.only(0,0,0,0))
    # ret_exp.subtitle = ft.Text(one_task['task_description'] + '\n' + '|', padding.only(0,0,0,0))
    ret_exp.title = ft.Text(one_task['task_name'], theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    ret_exp.subtitle = ft.Row(
        # todo: find a way to align the buttons vertically equal to the task name for the buttons
        #  below
        [
            ft.Text(one_task['task_description'], italic=True),
            ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
            ft.IconButton(icons.HIGHLIGHT_REMOVE),
        ],
        # alignment=ft.MainAxisAlignment.END,
    )
    # ret_exp.tile_padding = padding.only(task_padding + 10,5,5,5)
    ret_exp.controls_padding = padding.only(task_padding + 10, 5, 5, 5)
    if len(one_task['task_subtasks']) != 0:
        for subtask in one_task['task_subtasks']:
            ret_exp.controls.append(create_one_task_ui(subtask))
    return ret_exp


def create_one_task_card_ui(one_task: dict) -> ft.Card:
    task_control_buttons = ft.Column(
        spacing=0,
        controls=[
            ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
            ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
            ft.IconButton(icons.HIGHLIGHT_REMOVE),
        ],
    )

    task_info = ft.Column(
        spacing=0,
        wrap=True,
        alignment=MainAxisAlignment.START,
        horizontal_alignment=CrossAxisAlignment.START,
        controls=[
            ft.Text('Task name', no_wrap=False),
            ft.Row(
                wrap=True,
                controls=[
                    ft.Text("Music by Julie Gable. Lyrics by Sidney Stein.Music by Julie Gable. Lyrics by Sidney Stein."
                            # "Music by Julie Gable. Lyrics by Sidney Stein.Music by Julie Gable. Lyrics by Sidney Stein.Music by "
                            # "Julie Gable. Lyrics by Sidney Stein.Music by Julie Gable. Lyrics by Sidney Stein.", no_wrap=True
                            )
                ])
        ])
    # task_info.alignment = MainAxisAlignment.START
    # task_info.alignment = CrossAxisAlignment.START

    one_task_card = ft.Card(
        content=ft.Container(ft.Row(
            spacing=0,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment= CrossAxisAlignment.START,
            wrap=False,
            controls=[
                task_control_buttons,
                task_info,
                task_control_buttons,
            ],
        )))
    return one_task_card


# def create_task_cards_list_ui(all_tasks: dict) ->


def create_tasks_list_ui(all_tasks: dict) -> ft.Column:
    main_wrapper = ft.Column()
    for task in all_tasks['all_tasks']:
        one_card = ft.Card()
        one_card.content = create_one_task_ui(task)
        main_wrapper.controls.append(one_card)
    return main_wrapper


def main(page: Page):
    t_ui = create_tasks_list_ui(tsk.load_tasks())
    page.add(t_ui)
    for i in range(3):
        page.add(create_one_task_card_ui(dict_storage))


app(target=main)
