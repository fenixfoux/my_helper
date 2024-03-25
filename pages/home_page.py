import flet as ft


def change_route(e: ft.RouteChangeEvent):
    e.page.route = e.control.key
    e.page.update()


def main():
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
        ]
    )
    return content_page


if __name__ == '__main__':
    main()
