import datetime

import flet as ft

from pages.home_page import change_route
from pages.one_task import OneTask
import storages.all_variables as all_vars
from db_functionality import todo_db_funcs as db_td
from testing import example


class TodoComponents(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.selected_language = 'eng'
        self.list_tab_names = all_vars.all_tab_names[self.selected_language]
        self.link_to_searched_element = None
        self.all_tasks = db_td.get_all_tasks()  # task's objects

        self.new_task_creation_section = self.create_new_task_section()
        self.all_tabs = self.create_tabs_section()
        self.content_page = ft.Column()

        self.update_tabs_content()
        self.main()

    def one_task_card(self, received_task_object: OneTask):
        task_id_field = ft.Text(
            key=all_vars.key_task_id,
            value=str(received_task_object.task_id),
            visible=False
        )
        task_info_title_field = ft.Text(received_task_object.task_name)
        task_info_subtitle_field = ft.Text(
            value=received_task_object.task_description,
            italic=True
        )
        task_id = task_id_field.value

        if int(received_task_object.task_is_favorite) == 1:
            is_favorite_icon_color = ft.colors.ORANGE_500
        else:
            is_favorite_icon_color = None

        task_control_buttons = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            ft.icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED,
                            on_click=lambda e: self.task_done(e, task_id),
                            tooltip="change task status"
                        ),
                        ft.IconButton(
                            ft.icons.HIGHLIGHT_REMOVE,
                            on_click=lambda e: self.delete_selected_task(e, task_id),
                            data=task_id,
                            tooltip="delete this task"
                        ),
                    ],
                ),
                # example(),
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(  # edit current task
                            ft.icons.REBASE_EDIT,
                            # on_click=lambda e: self.edit_current_task(
                            #     e,
                            #     new_task_name=task_info_title_field.value,
                            #     new_task_description=task_info_subtitle_field.value,
                            #     task_id=task_id
                            # ),
                            tooltip="edit this task"
                        ),

                        # ft.IconButton(  # add a subtask
                        #     icons.ADD,
                        #     # on_click=lambda e: self.save_new_task(e, 'lll', 'imper', task_id)
                        # ),
                        ft.IconButton(
                            ft.icons.START,
                            tooltip="go to this task's page"
                        ),
                        ft.IconButton(
                            ft.icons.STAR,
                            tooltip="favorite?",
                            icon_color=is_favorite_icon_color,
                            on_click=lambda e: self.task_favorite(e, task_id),
                        ),
                    ],
                )
            ]
        )
        task_date = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(controls=[ft.Text(f"Created: {received_task_object.task_created_date}")]),
                ft.Row(controls=[ft.Text(f"Deadline: {received_task_object.task_due_date}")]),
            ]
        )
        task_status = ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.Text(
                    f"{all_vars.all_tab_names[self.selected_language][str(received_task_object.task_status)]}",
                    color=ft.colors.GREEN,
                    tooltip="task status")
            ]
        )
        task_info = ft.ListTile(
            title=ft.Column(controls=[
                task_status,
                task_info_title_field,
                task_info_subtitle_field
            ]),
            subtitle=task_date
        )

        one_task_card = ft.Card(
            content=ft.Column(
                spacing=0,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                wrap=False,
                controls=[
                    task_id_field,
                    task_control_buttons,
                    # task_status,
                    task_info,
                ],
            ))
        return one_task_card

    # def find_by_key(self, rec_elem, rec_key):
    #     """
    #     take current page view by using event (e.page.views[-1]) and search ft.Text field with received key 'rec_key',
    #     if element is found then his parent should be assigned to the TodoComponents attribute
    #     self.link_to_searched_element, after that the function which called that function can operate with
    #     searched element
    #     :param rec_elem: received element (e.page.views[-1])
    #     :param rec_key: received key (ft.control with that key should be found)
    #     :return:
    #     """
    #     if rec_elem.controls:
    #         # print(rec_elem.controls)
    #         for one_element in rec_elem.controls:
    #             # print(f"the key of current element is: '{one_element.key}'")
    #             if hasattr(one_element, 'key'):
    #                 if one_element.key == rec_key:
    #                     print(f"the element with searched key '{rec_key}' found.\n"
    #                           f"type of searched element is '{rec_elem}'\n"
    #                           f"element: {rec_elem}")
    #                     self.link_to_searched_element = rec_elem
    #
    #                 if hasattr(one_element, 'controls'):
    #                     # print(f"element {one_element} has controls")
    #                     self.find_by_key(one_element, rec_key)
    #                 else:
    #                     pass
    #                 # print(f"element {one_element} don't have controls")
    #     else:
    #         pass

    def find_by_key(self, rec_elem, rec_key):
        """
        take current page view by using event (e.page.views[-1]) and search ft.Text field with received key 'rec_key',
        if element is found then his parent should be assigned to the TodoComponents attribute
        self.link_to_searched_element, after that the function which called that function can operate with
        searched element
        :param rec_elem: received element (e.page.views[-1])
        :param rec_key: received key (ft.control with that key should be found)
        :return:
        """
        if rec_elem.controls:
            # print(rec_elem.controls)
            for one_element in rec_elem.controls:
                # print(f"the key of current element is: '{one_element.key}'")
                if hasattr(one_element, 'key'):
                    if one_element.key == rec_key:
                        # print(f"the element with searched key '{rec_key}' found.\n"
                        #       f"type of searched element is '{rec_elem}'\n"
                        #       f"element: {rec_elem}")
                        self.link_to_searched_element = rec_elem
                        break
                    if hasattr(one_element, 'controls'):
                        # print(f"element {one_element} has controls")
                        self.find_by_key(one_element, rec_key)
                    else:
                        pass
                    # print(f"element {one_element} don't have controls")
        else:
            pass

    def task_done(self, e, task_id):
        for task in self.all_tasks:
            if task.task_id == int(task_id):
                current_task = task

        if int(current_task.task_status) == 0:
            next_status = 1
        else:
            next_status = 0

        def callback_function(result):
            if result:
                if int(current_task.task_status) == 0:
                    current_task.task_status = 1
                else:
                    current_task.task_status = 0
                db_td.update_task(current_task)
                self.all_tasks = db_td.get_all_tasks()
                self.update_tabs_content()
                self.content_page.update()

        self.modal_confirm_dialog(
            e,
            f"change status to {all_vars.all_tab_names[self.selected_language][str(next_status)]}",
            callback_function)

    def task_favorite(self, e, task_id):
        for task in self.all_tasks:
            if task.task_id == int(task_id):
                current_task = task
                if int(current_task.task_is_favorite) == 0:
                    current_task.task_is_favorite = 1
                else:
                    current_task.task_is_favorite = 0
                db_td.update_task(current_task)
                self.update_tabs_content()
                self.content_page.update()

    def delete_selected_task(self, e, task_id):
        def callback_function(result):
            if result:
                elem_found = False
                for tab_content in self.all_tabs.tabs:
                    for item in tab_content.content.controls:
                        if isinstance(item, ft.Card):
                            for card_elem in item.content.controls:
                                if hasattr(card_elem, 'key'):
                                    if card_elem.key == all_vars.key_task_id:
                                        if card_elem.value == task_id:
                                            tab_content.content.controls.remove(item)
                                            self.all_tabs.update()
                                            elem_found = True
                if elem_found:
                    db_td.remove_task_by_id(task_id)
                    self.all_tasks = db_td.get_all_tasks()

        self.modal_confirm_dialog(e, 'delete task', callback_function)

    def create_new_task_section(self):
        new_task_name_field = ft.TextField(
            label=all_vars.new_task_name_hint_eng,
            hint_text=all_vars.new_task_name_hint_eng,
            # key=all_vars.key_new_task_name
        )
        new_task_description_field = ft.TextField(
            label=all_vars.new_task_description_hint_eng,
            hint_text=all_vars.new_task_description_hint_eng,
            # key=all_vars.key_new_task_description
        )
        due_date_field = ft.Text(str(datetime.date.today()),
                                 key=all_vars.key_due_date_field)
        date_picker = ft.DatePicker(
            on_change=lambda e: self.change_date(e, due_date_field),
            # on_dismiss=date_picker_dismissed,
            first_date=datetime.datetime(2023, 10, 1),
            last_date=datetime.datetime(2999, 10, 1),
        )
        date_button = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: date_picker.pick_date(),
        )
        due_date_section = ft.Row(
            controls=[
                ft.Text(all_vars.all_field_texts[self.selected_language]['due_date_text']),
                due_date_field,
                date_button
            ]
        )
        return ft.Column(
            # key=all_vars.key_section_new_task_creation,
            controls=[
                ft.Text(key=all_vars.key_section_new_task_creation, visible=False),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.ElevatedButton(
                            all_vars.button_back_text_eng,
                            key='/',
                            on_click=lambda ev: change_route(ev),
                            # on_click=lambda ev: print(ev.page)
                            # on_click=lambda ev: self.go_home(ev)
                        )
                    ]),
                new_task_name_field,
                new_task_description_field,
                date_picker,
                due_date_section,
                # date_button,
                # self.data_picker(),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text=all_vars.save_text_eng,
                            on_click=lambda e: self.save_new_task(
                                e,
                                t_name=new_task_name_field.value,
                                t_description=new_task_description_field.value,
                                task_created_date=datetime.date.today(),
                                task_due_date=due_date_field.value
                            )

                        ),
                        ft.ElevatedButton(
                            text=all_vars.clear_fields_new_task_button_text_eng,
                            on_click=lambda e: self.clear_new_task_section_fields(e, self.new_task_creation_section)
                        ),
                        ft.ElevatedButton(
                            all_vars.test_button_text_eng,
                            on_click=lambda e: self.test_func(e)
                        ),
                    ]
                )
            ])

    def clear_new_task_section_fields(self, ev, section_controls):
        for field in section_controls.controls:
            if isinstance(field, ft.TextField):
                field.value = ''
            if isinstance(field, ft.Column) or isinstance(field, ft.Row):
                self.clear_new_task_section_fields(ev, field)
            if isinstance(field, ft.Text) and hasattr(field, 'key'):
                if field.key == all_vars.key_due_date_field:
                    field.value = str(datetime.date.today())

        ev.control.page.update()

    def change_date(self, e, t_due_date_field):
        t_due_date_field.value = e.control.value.date()
        t_due_date_field.update()

    def modal_alert_dialog(self, ev, alert_text: str):
        dlg = ft.AlertDialog(
            title=ft.Text(alert_text), on_dismiss=lambda event: print("Dialog dismissed!")
        )
        ev.control.page.dialog = dlg
        dlg.open = True
        ev.control.page.update()

    def modal_confirm_dialog(self, ev, alert_text, callback):
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Confirm the operation"),
            content=ft.Text(f"Do you really want to {alert_text} ?"),
            actions=[
                ft.TextButton("Yes", on_click=lambda e: close_dlg(e, True)),
                ft.TextButton("No", on_click=lambda e: close_dlg(e, False)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        ev.control.page.dialog = dlg
        dlg.open = True
        ev.control.page.update()

        def close_dlg(e, confirmed: bool):
            dlg.open = False
            e.control.page.update()
            callback(confirmed)

    def test_func(self, e):
        print(f"test button was pressed")

    def create_list_of_task_cards(self, status: str = None) -> ft.Column:
        """
        create cards (ft.Card) for each task from list of all tasks (self.all_tasks) and put them into a column which
        is returned. if the 'status' is passed then add only tasks with passed status
        :param status:
        :return: control ft.Column with list of controls (ft.Card)
        """
        list_of_cards = ft.Column()
        list_of_cards.scroll = ft.ScrollMode.AUTO
        for one_task in self.all_tasks:
            # print(f"one_task.task_is_favorite: {one_task.task_is_favorite} type: {type(one_task.task_is_favorite)}")
            # print()
            # that case is for fill the tab which contain all tasks
            if status == all_vars.all_tab_names[self.selected_language][status]:
                one_card = self.one_task_card(received_task_object=one_task)
                list_of_cards.controls.append(one_card)
            # that case is for fill the tab which contain only tasks with passed status
            elif one_task.task_status == status:
                one_card = self.one_task_card(received_task_object=one_task)
                list_of_cards.controls.append(one_card)
            # that case is for fill the tab which contain only favorite tasks
            # elif one_task.task_is_favorite == "1" and status == 'favorite':
            #     one_card = self.one_task_card(received_task_object=one_task)
            #     list_of_cards.controls.append(one_card)

            print(one_task.task_is_favorite == "1")

            # elif status == all_vars.all_tab_names[self.selected_language][status] and is_favorite is not None:
            #     list_of_cards.controls.append(ft.Text('ololosh'))
        return list_of_cards

    def create_tabs_section(self):
        # функция которая должна создать UI в форме табов, количество вкладок соответствует элементам списка
        # self.tab_pages
        all_tabs = ft.Tabs(height=400)
        for one_tab_name in self.list_tab_names:
            all_tabs.tabs.append(
                ft.Tab(
                    text=self.list_tab_names[one_tab_name],
                    content=ft.Column()
                )
            )
        return all_tabs

    def update_tabs_content(self):
        """
        update content for every tab in all tabs, after call this function is required to use self.content_page.update()
        because that function update only the content of tabs not the Ui
        :return: None
        """
        # todo: actually update statement get list of all tasks, create list of cards with them and replace old tasks
        #  with the new tasks, that way is ok but it create uncomfortable view of refresh, and need to scroll again
        #  for find changed task. would be fine to find a way to change the element directly.
        created_list_cards = []
        for tab in self.all_tabs.tabs:
            for elem in all_vars.all_tab_names[self.selected_language]:
                if all_vars.all_tab_names[self.selected_language][elem] == tab.text:
                    created_list_cards = self.create_list_of_task_cards(status=elem)
            tab.content = created_list_cards

    def save_new_task(self, e, t_name, t_description, task_created_date, task_due_date, parent_task_id=None):
        """
        take data for creation one new task object, save it into database, append him to the page if is not a child task
        :param e: event handler
        :param t_name: str: text from field task name
        :param t_description: str: text from field task description
        :param task_created_date: str/date: system date creation date
        :param task_due_date: str/date: selected value in calendar
        :param parent_task_id: str: id of parent task, if new task then value is None
        :return: None
        """
        new_task = OneTask()
        new_task.task_name = t_name.strip()
        new_task.task_description = t_description
        new_task.task_created_date = task_created_date
        new_task.parent_task_id = parent_task_id

        if isinstance(task_due_date, str):
            datetime_obj = datetime.datetime.strptime(task_due_date, "%Y-%m-%d")
            new_task.task_due_date = datetime_obj.date()
        # todo: check if selected due date isn't expired, and if set expired date ask confirmation for set the status
        #  as 'completed' or 'active'
        new_task.task_due_date = task_due_date

        # check for empty task name
        if new_task.task_name:
            db_td.save_new_task(new_task)
            # update list of all tasks from database
            self.all_tasks = db_td.get_all_tasks()
            # print(f"type: {type(self.all_tasks[-1].task_status)}")
            self.clear_new_task_section_fields(e, self.new_task_creation_section)
            self.update_tabs_content()
            self.content_page.update()
        else:
            self.modal_alert_dialog(e, all_vars.alert_empty_task_name_eng)

    def main(self):
        self.content_page.controls.append(ft.Text(all_vars.todo_page_name_eng))
        self.content_page.controls.append(self.new_task_creation_section)
        self.content_page.controls.append(
            ft.ElevatedButton(
                key='/',
                text='go home',
                on_click=lambda ev: change_route(ev),
            )
        )
        self.content_page.controls.append(self.all_tabs)
