from flet import Container, Column, Text, TextButton


def main_page_content(page):
    return Container(
        content=Column(
            controls=[
                Text(value='Main page content'),
                TextButton('Todo page', on_click=lambda _: page.go('/todo_page')),
                TextButton('Temp one task page', on_click=lambda _: page.go('/temp_one_task_page')),
                TextButton('go to page 2', on_click=lambda _: page.go('/page_2')),
                TextButton('Todo page before changes', on_click=lambda _: page.go('/todo_page_before_changes'))
            ]
        )
    )

