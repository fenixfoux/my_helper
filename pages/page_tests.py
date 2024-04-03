import flet as ft
from pages.home_page import change_route


class PageTest(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.temp_list = ['one', 'two', 'three']
        self.test_section = ft.Column()
        self.content_page = ft.Column()

        self.append_content_in_section()
        self.main()

    def append_content_in_section(self):
        for element in self.temp_list:
            self.test_section.controls.append(
                ft.Text(element)
            )


    def main(self):
        self.content_page.controls.append(ft.Text('test page'),)
        self.content_page.controls.append(
            ft.ElevatedButton(
                key='/',
                text='go home',
                on_click=lambda ev: change_route(ev)
            ),
        )
        self.content_page.controls.append(self.test_section)

        # content = ft.Column(
        #     controls=[
        #         ft.Text('test page'),
        #         ft.ElevatedButton(
        #             key='/',
        #             text='go home',
        #             on_click=lambda ev: change_route(ev)
        #         ),
        #     ]
        # )
        # return content
