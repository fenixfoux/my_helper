import flet as ft

from pages.home_page import HomePage as main_h
from pages.page_1 import Page1 as main_p1
from pages.page_2 import main as main_p2

from pages.page_tests import PageTest as p_tests
from pages.todo_ui_components import TodoComponents as tc

def page_route_change_handler(page):
    page_home = main_h().main()
    # page_1 = main_p1().main()
    page_2 = main_p2()

    page_1 = tc().content_page
    # page_tests = p_tests().main()
    page_tests = p_tests().content_page

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
        '/page_tests': ft.View(
            "page_tests",
            [page_tests],
            scroll=ft.ScrollMode.AUTO
        ),
    }

    page.views.clear()
    page.views.append(
        pages[page.route]
    )
    page.update()


# if __name__ == '__main__':
#     page_route_change_handler(ft.Page)
