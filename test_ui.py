import flet as ft
from flet import *
import all_variables as all_vars


class TodoTaskPageUI(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.some_value = ""
        self.page_name = all_vars.page_name_eng
        self.tab_page_names = all_vars.all_tab_names_eng
        self.all_tasks = all_vars.default_list_of_tasks  # список словарей с задачами
        # self.new_tasks_section_controls = self.create_new_task_section()

        self.new_task_name_field = None
        self.new_task_description_field = None
        self.all_tabs = None

    def create_new_task_section(self):
        self.new_task_name_field = TextField(hint_text=all_vars.new_task_name_hint_eng)
        self.new_task_description_field=ft.TextField(hint_text=all_vars.new_task_description_hint_eng)
        return ft.Column([
            ft.Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(self.page_name),
                    ft.ElevatedButton(all_vars.button_back_text_eng)
                ]),
            self.new_task_name_field,
            self.new_task_description_field,
            ft.Row(
                controls=[
                    ft.ElevatedButton(all_vars.save_new_task_button_text_eng),
                    ft.ElevatedButton(
                        text=all_vars.clear_fields_new_task_button_text_eng,
                        on_click=self.clear_new_task_section_fields),
                    ft.ElevatedButton(all_vars.test_button_text_eng),
                ]
            )
        ])
        # функция которая должна создавать UI с двумя полями для ввода текста и двумя кнопками, сохранить задачу и
        # очистить поля

    def clear_new_task_section_fields(self, e):
        self.new_task_name_field.value = ''
        self.new_task_description_field.value = ''
        self.new_task_name_field.update()
        self.new_task_description_field.update()
        # todo: find a way to clean and update all fields all immediately not one by one

    def create_one_task_card_ui(self, one_task: dict) -> ft.Card:
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

    def create_tabs_section(self):
        # функция которая должна создать UI в форме табов, количество вкладок соответствует элементам списка
        # self.tab_pages
        self.all_tabs = ft.Tabs()
        for one_tab_name in self.tab_page_names:
            self.all_tabs.tabs.append(
                self.update_tasks(tab_name=one_tab_name)
            )
        return self.all_tabs

    def save_new_task(self):
        # функция сохранения новой задачи в общий список всех задач, эта функция должна срабатывать при нажатии на
        # кнопку сохранить так же при сохранении новой задачи должна будет вызываться функция update_tasks которая
        # будет обновлять UI
        pass

    def update_tasks(self, tab_name):
        # функция заполнения одного Tab-а в Tabs, эта функция должна смотреть в self.all_tasks и для каждого task
        # создать текстовое поле в котором выведет данные
        # return pg
        tab_wrapper = ft.Column()
        for one_task in self.all_tasks['all_tasks']:
            tab_wrapper.controls.append(self.create_one_task_card_ui(one_task))
        return ft.Tab(
            text=tab_name,
            content=tab_wrapper
        )

    def create_todo_task_page(self):
        created_page = ft.Column(controls=[
            self.create_new_task_section(),
            self.create_tabs_section(),
        ])

        return created_page


# ===== TESTING ===== #
def main(page: Page):
    todo_tp = TodoTaskPageUI()
    page.add(todo_tp.create_todo_task_page())


ft.app(target=main)
