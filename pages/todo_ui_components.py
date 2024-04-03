import datetime

import flet as ft

from pages.home_page import change_route
from pages.one_task import OneTask
import storages.all_variables as all_vars
from db_functionality import todo_db_funcs as db_td


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
        task_info_title_field = ft.Text(received_task_object.task_name, key='task_name')
        task_info_subtitle_field = ft.Text(
            value=received_task_object.task_description,
            key='task_description',
            italic=True
        )
        task_id = task_id_field.value
        task_control_buttons = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(ft.icons.PLAYLIST_ADD_CHECK_CIRCLE_OUTLINED),
                        ft.IconButton(
                            ft.icons.HIGHLIGHT_REMOVE,
                            on_click=lambda e: self.delete_selected_task(e, task_id),
                            data=task_id),
                    ],
                ),
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
                            # )
                        ),

                        # ft.IconButton(  # add a subtask
                        #     icons.ADD,
                        #     # on_click=lambda e: self.save_new_task(e, 'lll', 'imper', task_id)
                        # ),
                        ft.IconButton(ft.icons.START),
                        ft.IconButton(ft.icons.STAR),
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
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                wrap=False,
                controls=[
                    task_id_field,
                    task_control_buttons,
                    task_info
                ],
            ))
        return one_task_card

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
                        print(f"the element with searched key '{rec_key}' found.\n"
                              f"type of searched element is '{rec_elem}'\n"
                              f"element: {rec_elem}")
                        self.link_to_searched_element = rec_elem

                    if hasattr(one_element, 'controls'):
                        # print(f"element {one_element} has controls")
                        self.find_by_key(one_element, rec_key)
                    else:
                        pass
                    # print(f"element {one_element} don't have controls")

        else:
            pass

    def delete_selected_task(self, e, task_id):
        current_page = e.page.views[-1]
        # find the block with list of cards and assign the result to self.list_of_cards
        self.find_by_key(current_page, all_vars.key_list_of_cards)
        # search in block list of cards and delete the card by id
        print('=' * 50)
        for item in self.link_to_searched_element.controls:
            # print(item)
            # print(isinstance(item, ft.Card))
            if isinstance(item, ft.Card):
                for field in item.content.controls:  # find field with key 'task_id'
                    print(field.key)
                    if field.key is not None:
                        if field.key == all_vars.key_task_id:
                            if field.value == task_id:
                                self.link_to_searched_element.controls.remove(item)
                                e.control.page.update()

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
        due_date_field = ft.Text(str(datetime.date.today()))
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
                ft.Text(all_vars.due_date_text_eng),
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
                                task_due_date=due_date_field.value
                            )

                        ),
                        ft.ElevatedButton(
                            text=all_vars.clear_fields_new_task_button_text_eng,
                            # on_click=self.clear_new_task_section_fields
                        ),
                        ft.ElevatedButton(
                            all_vars.test_button_text_eng,
                            on_click=lambda e: self.test_func(e)
                        ),
                    ]
                )
            ])

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

    def test_func(self, e):
        print('test button pressed')
        current_page = e.page.views[-1]

        self.modal_alert_dialog(e, 'krya')

        # find the new task creation section control by key
        self.find_by_key(current_page, all_vars.key_section_new_task_creation)

        print(self.link_to_searched_element)
        print(self.link_to_searched_element.controls)

    def create_list_of_task_cards(self, status: str = None) -> ft.Column:
        """
        create cards (ft.Card) for each task from list of all tasks (self.all_tasks) and put them into a column which
        is returned. if the 'status' is passed then add only tasks with passed status
        :param status:
        :return: control ft.Column with list of controls (ft.Card)
        """
        list_of_cards = ft.Column()
        for one_task in self.all_tasks:
            if status is None:
                one_card = self.one_task_card(received_task_object=one_task)
                list_of_cards.controls.append(one_card)
            elif one_task.task_status == status:
                one_card = self.one_task_card(received_task_object=one_task)
                list_of_cards.controls.append(one_card)
        list_of_cards.controls.append(ft.Text(key=all_vars.key_list_of_cards, visible=False))
        return list_of_cards

    def create_tabs_section(self):
        # функция которая должна создать UI в форме табов, количество вкладок соответствует элементам списка
        # self.tab_pages
        all_tabs = ft.Tabs(height=400, )
        for one_tab_name in self.list_tab_names:
            all_tabs.tabs.append(
                ft.Tab(
                    text=self.list_tab_names[one_tab_name],
                    content=ft.Text('')
                )
            )
        return all_tabs

    def update_tabs_content(self):
        print(self.all_tabs.tabs)
        counter = 0
        for tab in self.all_tabs.tabs:
            counter += 1
            # print(tab.text)
            if tab.text == "all":
                created_list_cards = self.create_list_of_task_cards()
            else:
                created_list_cards = self.create_list_of_task_cards(status=tab.text)
            tab.content = created_list_cards

    def save_new_task(self, e, t_name, t_description, task_due_date):
        new_task = OneTask()
        new_task.task_name = t_name.strip()
        new_task.task_description = t_description

        if isinstance(task_due_date, str):
            datetime_obj = datetime.datetime.strptime(task_due_date, "%Y-%m-%d")
            new_task.task_due_date = datetime_obj.date()
        # todo: check if selected due date isn't expired
        new_task.task_due_date = task_due_date
        # print(new_task.task_name)
        # print(new_task.task_description)
        # print(f"new_task.task_due_date: {new_task.task_due_date}")
        # print(f"type(new_task.task_due_date): {type(new_task.task_due_date)}")
        # print(new_task.task_due_date >= datetime.date.today())

        # check for empty task name
        if new_task.task_name:
            # todo: save in data base
            # todo: add to the list of existing widgets
            print('+++++')
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
