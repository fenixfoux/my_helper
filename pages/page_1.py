import flet as ft
from pages.home_page import change_route
import db_functionality.todo_db_funcs as db_f
from pages.one_task import OneTask
from pages.todo_ui_components import TodoComponents as tc
import storages.all_variables as all_vars


class Page1(ft.UserControl):
    def __init__(self):
        super().__init__()
        pass
        # self.all_tasks_list = db_f.get_all_tasks()
        # self.created_list_of_cards = self.card_list_of_tasks()

    # def card_list_of_tasks(self):
    #     list_of_cards = ft.Column()
    #     for one_task in self.all_tasks_list:
    #         one_card = tc().one_task_card(received_task_object=one_task)
    #         list_of_cards.controls.append(one_card)
    #     list_of_cards.controls.append(ft.Text(key=all_vars.key_list_of_cards, visible=False))
    #     return list_of_cards

    def main(self):
        # list_of_tabs = tc().create_tabs_section()
        # print(f"="*99,"\n",
        #       f"{tc().all_tabs}\n",
        #       f"="*99)
        content_page = ft.Column(
            controls=[
                ft.Text(all_vars.todo_page_name_eng),
                tc().create_new_task_section(),
                ft.ElevatedButton(
                    key='/',
                    text='go home',
                    on_click=lambda ev: change_route(ev),
                ),
                tc().all_tabs,
                # tc().update_tabs_content(tc().all_tabs),
            ]
        )
        return content_page


# if __name__ == '__main__':
#     Page1().main()
