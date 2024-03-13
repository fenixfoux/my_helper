import flet as ft
import todo_code.auxiliary_functions as aux_f
from flet import *
from storage import all_variables as all_vars
from todo_code import tasks_refactored as tsk
from storage.all_variables import new_task_creation


class OneTaskPage(ft.UserControl):
    def __init__(self, received_task):
        super().__init__()
        self.received_task = received_task
        self.confirm_alert_dialog = None

    def header_section(self):
        header_section = ft.Row(tight=True)
        header_content_part = ft.Column(expand=9, key='header_content_part')
        header_buttons_part = ft.Column(expand=1)
        for key in self.received_task:
            visible = True
            if key != 'task_subtasks':
                if key == 'task_id':
                    visible = False
                header_content_part.controls.append(ft.Text(key=key, value=self.received_task[key], visible=visible))

        header_buttons_part.controls.append(
            ft.ElevatedButton('test',
                              on_click=lambda event: self.create_modify_task_alert_dialog(event, header_content_part)))
        header_section.controls = [header_content_part, header_buttons_part]
        return header_section

    def create_modify_task_alert_dialog(self, e, content: ft.Column):
        print(content.key)
        temp_dict = {}
        for item in content.controls:
            temp_dict[item.key] = item.value

        created_alert_dialog = ft.AlertDialog(modal=True)
        prepared_content = ft.Column(tight=True)
        prepared_actions = ft.Row(
            controls=[
                ft.TextButton('Modify', on_click=lambda ev: modify_task(ev, prepared_content.controls)),
                ft.TextButton('Cancel')
            ]
        )
        for field in temp_dict:
            visible = True
            if field == 'task_id':
                visible = False
            prepared_content.controls.append(ft.TextField(
                value=temp_dict[field],
                visible=visible,
            ))

        created_alert_dialog.content = prepared_content
        created_alert_dialog.actions = prepared_actions.controls

        def modify_task(ev, list_controls):
            nonlocal temp_dict
            for one_item, one_control in zip(temp_dict, list_controls):
                temp_dict[one_item] = one_control.value

            # todo: function to modify task in storage file
            # todo: function to modify UI on page
            self.update_ui_by_key(event=ev, section_key=content.key, dict_to_ui=temp_dict)

            created_alert_dialog.open = False
            ev.control.page.update()

        def open_dlg_modal(ev):
            ev.control.page.dialog = created_alert_dialog
            created_alert_dialog.open = True
            ev.control.page.update()

        open_dlg_modal(e)

    def update_ui_by_key(self, event, section_key, dict_to_ui: dict):
        """
        take section name, and dictionary, search on page the section withe key as received to find, once found modify
        fields with values from received dictionary if field key is the same as dictionary row key
        :param event:
        :param section_key: section name
        :param dict_to_ui: dictionary with modified values
        :return:
        """
        def find_field_by_key(e, key: str, controls):
            for field in controls:
                if field.key == key:
                    print(f"field with key '{key}' found: '{field}'")
                    # if section found then update fields in that section by keys in received modified dictionary:
                    for one_field, one_value in zip(field.controls, dict_to_ui):
                        if one_field.key == one_value:
                            one_field.value = dict_to_ui[one_value]
                    e.control.page.update()
                    break
                try:
                    if field.controls:
                        find_field_by_key(e, key, field.controls)
                except AttributeError:
                    pass

        find_field_by_key(event, section_key, event.control.page.controls)

    def create_one_task_page(self):
        return ft.Column(
            controls=[
                self.header_section()
            ]
        )


# ===== TESTING ===== #
def main(page: Page):
    # check_storage_file()
    todo_tp = OneTaskPage(new_task_creation)
    page.add(todo_tp.create_one_task_page())


#
ft.app(target=main)
