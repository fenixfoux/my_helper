import flet as ft
from flet import *


# auxiliary_functions.py

# auxiliary_functions.py

def create_alert_dialog(e, confirmation_question: str):
    """
    create a modal window with ui : question to confirm or reject
    :param e: event
    :param confirmation_question: str, question for confirm or reject anything
    :return: bool, True if user pressed "Yes", False if pressed "No"
    """
    decision = None

    def callback(choice):
        nonlocal decision
        decision = choice

    created_alert_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text(f"Do you really want to {confirmation_question}"),
        actions=[
            ft.TextButton("Yes", on_click=lambda event: callback(True)),
            ft.TextButton("No", on_click=lambda event: callback(False)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    e.control.page.dialog = created_alert_dialog
    created_alert_dialog.open = True
    e.control.page.update()

    # Wait for the user to make a choice
    while decision is None:
        pass
    if decision is not None:
        created_alert_dialog.open = False
        e.control.page.update()

    return decision

def modify_task_alert_dialog(e, confirmation_question: str, task_dict: dict):
    """
    create a modal window with ui : question to confirm or reject
    :param e: event
    :param confirmation_question: str, question for confirm or reject anything
    :return: bool, True if user pressed "Yes", False if pressed "No"
    """
    decision = None
    modified_task = {}
    def callback(choice):
        nonlocal decision
        decision = choice

    created_alert_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("confirmation_question"),
        content=ft.Column(
            tight=True,
            controls=[
                ft.TextField(value=task_dict['task_name']),
                ft.TextField(value=task_dict['task_description']),
            ]
        ),
        actions=[
            ft.TextButton("Yes", on_click=lambda event: callback(True)),
            ft.TextButton("No", on_click=lambda event: callback(False)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    e.control.page.dialog = created_alert_dialog
    created_alert_dialog.open = True
    e.control.page.update()

    # Wait for the user to make a choice
    while decision is None:
        pass
    if decision is not None:
        created_alert_dialog.open = False
        e.control.page.update()

    return decision, modified_task




# def open_confirm_alert_dialog(e, dlg_modal: ft.AlertDialog):
#     """
#     open received confirmation dialog
#     :param e: event
#     :param dlg_modal: control, ft.AlertDialog
#     :return:
#     """
#     e.control.page.dialog = dlg_modal
#     dlg_modal.open = True
#     e.control.page.update()


# def decision_confirm_alert_dialog(e, dlg_modal: ft.AlertDialog, choice: bool) -> bool:
#     dlg_modal.open = False
#     e.control.page.update()
#     return choice
