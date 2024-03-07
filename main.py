from flet import *

from pages_ui.main_page import main_page_content as mpc
from pages_ui.todo_page import TodoTaskPageUI


# todo:
#  - if task name is empty alert dialog about that and don't create/update task
#  - before deleting task alert dialog with question yes/no
#  -
#  -


def main(one_page: Page):
    main_page_content = mpc(one_page)
    to_do_page_content = TodoTaskPageUI().create_todo_task_page()

    pages = {
        '/': View(
            "/",
            # [main_page_content],
            [to_do_page_content],  # todo: remove after end, now is for starts with todo_page
        ),
        '/todo_page': View(
            "todo_page",
            [to_do_page_content],
            scroll=ScrollMode.AUTO
        ),
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
