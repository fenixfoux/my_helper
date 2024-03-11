import flet as ft
from flet import *
from storage import all_variables as all_vars
from todo_code import tasks_refactored as tsk


class TodoTaskPageUI(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.created_page = None
        self.some_value = ""
        self.page_name = all_vars.page_name_eng
        self.tab_page_names = all_vars.all_tab_names_eng
        self.check_storage_file = tsk.check_storage_file()
        self.all_tasks = tsk.load_tasks()  # список словарей с задачами
        self.all_existed_keys = []
        # self.all_tasks = all_vars.default_list_of_tasks  # список словарей с задачами
        # self.new_tasks_section_controls = self.create_new_task_section()

        self.new_task_name_field = None
        self.new_task_description_field = None
        self.all_tabs = None

    def create_new_task_section(self) -> ft.Column:
        self.new_task_name_field = TextField(hint_text=all_vars.new_task_name_hint_eng)
        self.new_task_description_field = ft.TextField(hint_text=all_vars.new_task_description_hint_eng)
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
                    ft.ElevatedButton(
                        text=all_vars.save_new_task_button_text_eng,
                        on_click=lambda e: self.save_new_task(
                            e,
                            self.new_task_name_field.value,
                            self.new_task_description_field.value,
                            None,
                            all_vars.all_operation_types['add']
                        )

                    ),
                    ft.ElevatedButton(
                        text=all_vars.clear_fields_new_task_button_text_eng,
                        on_click=self.clear_new_task_section_fields),
                    ft.ElevatedButton(
                        all_vars.test_button_text_eng,
                        on_click=lambda e: self.test_func(e)
                    ),
                ]
            )
        ])
        # функция которая должна создавать UI с двумя полями для ввода текста и двумя кнопками (сохранить задачу и
        # очистить поля)

    def clear_new_task_section_fields(self, e):
        self.new_task_name_field.value = ''
        self.new_task_description_field.value = ''
        self.new_task_name_field.update()
        self.new_task_description_field.update()
        # todo: find a way to clean and update all fields all immediately not one by one

    def create_one_task_card_ui(self, one_task: dict) -> ft.Card:
        task_id_field = ft.Text(
            value=one_task['task_id'],
            visible=False
        )
        task_info_title_field = ft.Text(one_task['task_name'], key='task_name')
        task_info_subtitle_field = ft.Text(
            value=one_task['task_description'],
            key='task_description',
            italic=True
        )
        task_id = task_id_field.value
        task_control_buttons = ft.Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
                        ft.IconButton(
                            icons.HIGHLIGHT_REMOVE,
                            on_click=lambda e: self.delete_selected_task(e, task_id),
                            data=task_id),
                    ],
                ),
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(  # edit current task
                            icons.REBASE_EDIT,
                            on_click=lambda e: self.edit_current_task(
                                e,
                                new_task_name=task_info_title_field.value,
                                new_task_description=task_info_subtitle_field.value,
                                task_id=task_id
                            )
                        ),

                        # ft.IconButton(  # add a subtask
                        #     icons.ADD,
                        #     # on_click=lambda e: self.save_new_task(e, 'lll', 'imper', task_id)
                        # ),
                        ft.IconButton(icons.START),
                        ft.IconButton(icons.STAR),
                    ],
                )
            ]
        )

        task_info = ft.ListTile(
            title=task_info_title_field,
            subtitle=task_info_subtitle_field,
            key='task_info',
        )
        one_task_card = ft.Card(
            content=ft.Column(
                spacing=0,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                wrap=False,
                controls=[
                    task_id_field,
                    task_control_buttons,
                    task_info
                ],
            ))
        return one_task_card

    def create_tabs_section(self):
        # функция которая должна создать UI в форме табов, количество вкладок соответствует элементам списка
        # self.tab_pages
        self.all_tabs = ft.Tabs(height=400, )
        for one_tab_name in self.tab_page_names:
            self.all_tabs.tabs.append(
                self.load_tasks(tab_name=one_tab_name)
            )
        return self.all_tabs

    def save_new_task(self, e, new_task_name, new_task_description, parent_id=None, operation_type=''):
        # функция сохранения новой задачи в общий список всех задач, эта функция должна срабатывать при нажатии на
        # кнопку сохранить так же при сохранении новой задачи должна будет вызываться функция update_tasks которая
        # будет обновлять UI
        self.all_existed_keys = tsk.get_all_existing_keys(self.all_tasks, self.all_existed_keys)
        if new_task_name.strip():
            generated_unique_id = tsk.generate_unique_task_id(self.all_existed_keys)
            prepared_task_as_dict = tsk.prepare_new_task_dict(
                task_id=generated_unique_id,
                task_name=new_task_name,
                task_description=new_task_description,
            )
            tsk.create_task(
                all_tasks_list=self.all_tasks,
                new_task=prepared_task_as_dict
            )
            self.all_tasks = tsk.load_tasks()  # update list of all tasks
            # update UI by appending created new task if this is not a subtask
            if parent_id is None:
                created_task = tsk.find_task_by_id(self.all_tasks, generated_unique_id)
                for tab in self.all_tabs.tabs:
                    if tab.text == 'all':
                        tab_content = tab.content
                        # print(type(tab_content))
                        if isinstance(tab_content, ft.Column):
                            tab_content.controls.append(self.create_one_task_card_ui(created_task))
                            self.all_tabs.update()
                            break

            # update all existed keys
            self.all_existed_keys = tsk.get_all_existing_keys(self.all_tasks, self.all_existed_keys)
            self.clear_new_task_section_fields(e)

    def edit_current_task(self,
                          e,
                          new_task_name,
                          new_task_description,
                          task_id):
        """open modal dialog with inputs filled with task's data and allow to modify and save the task"""
        dlg_task_id_field = ft.Text(task_id)
        dlg_task_name_field = ft.TextField(value=new_task_name)
        dlg_task_description_field = ft.TextField(value=new_task_description)

        def modify_task_window_btn_yes(ev, upd_task_name, upd_task_description):
            if len(upd_task_name.strip()) != 0:
                dlg_modal.open = False
                # create updated task
                updated_task = tsk.prepare_new_task_dict(
                    task_id=task_id,
                    task_name=upd_task_name,
                    task_description=upd_task_description,
                )
                print(f"updated task: {updated_task}")
                # save updated task
                tsk.update_task(self.all_tasks, updated_task)
                # load updated list of tasks
                self.all_tasks = tsk.load_tasks()
                # update the card with new data
                for tab in self.all_tabs.tabs:
                    tab_content = tab.content
                    for one_card in tab_content.controls:
                        # one_card.content.controls[0] is a ft.Text which value contain the task_id
                        if one_card.content.controls[0].value == task_id:
                            for field in one_card.content.controls:
                                if field.key == 'task_info':
                                    print('kk')
                                    print(type(field))
                                    print(type(field.title.value))
                                    field.title.value = upd_task_name
                                    field.subtitle.value = upd_task_description
                            e.control.page.update()

                # print(self.all_tasks)
                ev.control.page.update()
            else:
                dlg_task_name_field.error_text = 'Input the fucking task name, maaaaan'
                ev.control.page.update()

        def close_dlg(ev):
            dlg_modal.open = False
            # for tab in self.all_tabs.tabs:
            #     if tab.text == 'all':
            #         tab_content = tab.content
            #         print(type(tab_content))
            #         if isinstance(tab_content, ft.Column):
            #             tab_content.controls.clear()

            ev.control.page.update()

        # dialog window for editing task
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("edit task"),
            content=ft.Column(
                tight=True,
                controls=[
                    dlg_task_id_field,
                    dlg_task_name_field,
                    dlg_task_description_field,
                ]
            ),
            actions=[
                ft.TextButton("Yes",
                              on_click=lambda e: modify_task_window_btn_yes(
                                  ev=e,
                                  upd_task_name=dlg_task_name_field.value,
                                  upd_task_description=dlg_task_description_field.value,
                              )),
                ft.TextButton("No", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            # on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        def open_dlg_modal(ev):
            ev.control.page.dialog = dlg_modal
            dlg_modal.open = True
            ev.control.page.update()

        open_dlg_modal(e)

        # return ft.IconButton(icons.ADD, on_click=open_dlg_modal)

    def delete_selected_task(self, e, task_id):
        print('delete task button was pressed')
        print(f"task id of this card is: {task_id}")
        tsk.delete_task(self.all_tasks, task_id)
        for tab in self.all_tabs.tabs:
            tab_content = tab.content
            for one_card in tab_content.controls:
                # one_card.content.controls[0] is a ft.Text which value contain the task_id
                if one_card.content.controls[0].value == task_id:
                    print(type(tab_content.controls))
                    print(len(tab_content.controls))
                    tab_content.controls.remove(one_card)
                    print(len(tab_content.controls))
                    # self.all_tabs.update()
                    e.control.page.update()

    def load_tasks(self, tab_name):
        # функция заполнения одного Tab-а в Tabs, эта функция должна смотреть в self.all_tasks и для каждого task
        # создать текстовое поле в котором выведет данные
        # return pg
        tab_wrapper = ft.Column(scroll=ScrollMode.AUTO)
        if tab_name == 'all':
            for one_task in self.all_tasks:
                tab_wrapper.controls.append(self.create_one_task_card_ui(one_task))
        return ft.Tab(
            text=tab_name,
            content=tab_wrapper
        )

    def create_todo_task_page(self):
        self.created_page = ft.Column(controls=[
            self.create_new_task_section(),
            self.create_tabs_section(),
        ])

        return self.created_page

    def test_press_get_value(self, e, task_id):
        print('icon button was pressed')
        print(f"type of 'e': {type(e)}")
        print(f"tas k id of this card is: {task_id}")

    def test_func(self, e):
        print('test func button pressed')
        # ft = tsk.find_task_by_id(self.all_tasks, 368743)

        print(ft)


# # ===== TESTING ===== #
# def main(page: Page):
#     # check_storage_file()
#     todo_tp = TodoTaskPageUI()
#     page.add(todo_tp.create_todo_task_page())
#
#
# #
# ft.app(target=main)
