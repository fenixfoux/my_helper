import flet as ft


def change_route(e: ft.RouteChangeEvent):
    e.page.route = e.control.key
    e.page.update()





class HomePage(ft.UserControl):
    def __init__(self):
        super().__init__()
        pass

    def main(self):
        content_page = ft.Column(
            controls=[
                ft.Text('home page'),
                ft.ElevatedButton(
                    key='/page_1',
                    text='go to page 1',
                    on_click=lambda ev: change_route(ev)
                ),
                ft.ElevatedButton(
                    key='/page_2',
                    text='go to page 2',
                    on_click=lambda ev: change_route(ev)
                ),
                ft.ElevatedButton(
                    key='/page_tests',
                    text='go to page test',
                    on_click=lambda ev: change_route(ev)
                ),
            ]
        )
        return content_page



# if __name__ == '__main__':
#     HomePage().main()
