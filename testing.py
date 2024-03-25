import flet as ft

from router import page_route_change_handler



def main(one_page: ft.Page):

    one_page.on_route_change = lambda _: page_route_change_handler(one_page)
    one_page.go(one_page.route)
    one_page.update()


ft.app(target=main)
