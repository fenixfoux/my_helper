import flet as ft

default_list_of_tasks = {
    "all_tasks": [
        {
            "task_id": 1,
            "task_name": "default task name",
            "task_description": "default description",
            "task_subtasks": []
        },
        {
            "task_id": 699130,
            "task_name": "task number 2",
            "task_description": "432142",
            "task_subtasks": [
                {
                    "task_id": 845182,
                    "task_name": "unnamed task",
                    "task_description": "unnamed description",
                    "task_subtasks": []
                },
                {
                    "task_id": 462169,
                    "task_name": "desfr",
                    "task_description": "aaaaa",
                    "task_subtasks": []
                }
            ]
        },
        {
            "task_id": 263379,
            "task_name": "task number 3",
            "task_description": "555",
            "task_subtasks": [
                {
                    "task_id": 66,
                    "task_name": "666666",
                    "task_description": "66",
                    "task_subtasks": []
                }
            ]
        }
    ]
}


def test(list_of_subtasks: list):
    created_subtasks_body = ft.ExpansionPanelList()

    def create_one_subtask_panel(one_subtask: dict, parent_panel: ft.ExpansionPanel = None):
        one_panel = ft.ExpansionPanel()
        one_panel.key = one_subtask['task_id']
        one_panel.header = ft.Text(value=one_subtask['task_name'])
        one_panel.content = ft.ListTile(
            title=ft.Text(value=one_subtask['task_description'])
        )

        if one_subtask['task_subtasks']:
            nested_panel_list = ft.ExpansionPanelList()  # Create a nested panel list for subtasks
            for sbt in one_subtask['task_subtasks']:
                create_one_subtask_panel(sbt, nested_panel_list)  # Recursively create nested panels
            one_panel.content = nested_panel_list  # Set the content of the current panel to the nested panel list

        if parent_panel:
            parent_panel.controls.append(one_panel)  # If a parent panel exists, append to it
        else:
            created_subtasks_body.controls.append(one_panel)  # Otherwise, append to the main panel list

    for subtask in list_of_subtasks:
        create_one_subtask_panel(subtask)  # Start with the top-level tasks
    return created_subtasks_body



# def example():
#     # def handle_change(e: ft.ControlEvent):
#     #     print(f"change on panel with index {e.data}")
#
#     def remove_subtask_by_id(e: ft.ControlEvent, subtask_key):
#         for one_subtask in panel.controls:
#             print(one_subtask)
#             if one_subtask.key == subtask_key:
#                 panel.controls.remove(e.control.data)
#                 panel.update()
#
#     panel = ft.ExpansionPanelList(
#         elevation=8,
#         controls=[],
#     )
#
#     for i in range(3):
#         exp = ft.ExpansionPanel(
#             header=ft.ListTile(title=ft.Text(f"Panel {i}")),
#         )
#         exp.content = ft.ListTile(
#             title=ft.Text(f"This is in Panel {i}"),
#             subtitle=ft.Text(f"Press the icon to delete panel {i}"),
#             trailing=ft.IconButton(ft.icons.DELETE,
#                                    on_click=lambda event: remove_subtask_by_id(event, exp.key, ),
#                                    data=exp),
#         )
#         exp.key = 'key_' + str(i)
#
#         panel.controls.append(exp)
#     return panel


def main(page):
    page.title = "Card Example"
    page.add(
        # example(),
        test(default_list_of_tasks['all_tasks']),
    )


ft.app(target=main)
