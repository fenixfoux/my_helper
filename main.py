import flet as ft
from flet import *
from main_page_content import create_main_page_content

from todo_page import TodoTaskPageUI

from second_page_content import create_second_page_content
from to_do_page_before_changes import create_to_do_page_content_before_changes


def main(one_page: Page):
    to_do_page_content = TodoTaskPageUI().create_todo_task_page()
    main_page_content = create_main_page_content(one_page)
    # to_do_page_content = create_to_do_page_content(one_page)
    second_page_content = create_second_page_content(one_page)
    todo_page_before_changes = create_to_do_page_content_before_changes()

    pages = {
        '/': View(
            "/",
            [main_page_content],
        ),
        '/todo_page': View(
            "todo_page",
            [to_do_page_content],
            scroll=ScrollMode.AUTO
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
        one_page.views.clear()
        one_page.views.append(
            pages[one_page.route]
        )
    one_page.add(main_page_content)

    one_page.on_route_change = route_change
    one_page.go(one_page.route)


app(target=main)
