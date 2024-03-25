import flet as ft

from pages.home_page import main as main_h
from pages.page_1 import main as main_p1
from pages.page_2 import main as main_p2


def page_route_change_handler(page):
    page_home = main_h()
    page_1 = main_p1()
    page_2 = main_p2()

    pages = {
        '/': ft.View(
            "/",
            [page_home],
            # [to_do_page_content],  # todo: remove after end, now is for starts with todo_page
        ),
        '/page_1': ft.View(
            "page_1",
            [page_1],
            scroll=ft.ScrollMode.AUTO
        ),
        '/page_2': ft.View(
            "page_2",
            [page_2],
            scroll=ft.ScrollMode.AUTO
        ),
    }

    page.views.clear()
    page.views.append(
        pages[page.route]
    )
    page.update()


if __name__ == '__main__':
    page_route_change_handler(ft.Page)
