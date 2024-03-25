import flet as ft
from pages.home_page import change_route


def main():
    content_page = ft.Column(
        controls=[
            ft.Text('page 1'),
            ft.ElevatedButton(
                key='/',
                text='go home',
                on_click=lambda ev: change_route(ev)
            ),
        ]
    )
    return content_page


if __name__ == '__main__':
    main()
