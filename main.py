import flet as ft
from flet import *
from main_page_content import create_main_page_content
from to_do_page import create_to_do_page_content
from second_page_content import create_second_page_content
from to_do_page_before_changes import create_to_do_page_content_before_changes


def main(page: Page):
    main_page_content = create_main_page_content(page)
    first_page_content = create_to_do_page_content()
    second_page_content = create_second_page_content(page)
    todo_page_before_changes = create_to_do_page_content_before_changes()

    pages = {
        '/': View(
            "/",
            [main_page_content],
        ),
        '/todo_page': View(
            "todo_page",
            [first_page_content],
        ),
        '/page_2': View(
            'page_2',
            [second_page_content]
        ),
        '/todo_page_before_changes': View(
            'todo_page_before_changes',
            [todo_page_before_changes]
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    page.add(main_page_content)

    page.on_route_change = route_change
    page.go(page.route)


app(target=main)
