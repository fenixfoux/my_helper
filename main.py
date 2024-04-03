import flet as ft

from router import page_route_change_handler
from db_functionality import todo_db_funcs as db_td


def main(one_page: ft.Page):
    db_td.check_for_db()

    one_page.on_route_change = lambda _: page_route_change_handler(one_page)
    one_page.go(one_page.route)
    one_page.update()

ft.app(target=main)
