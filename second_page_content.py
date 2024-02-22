# second_page_content.py
from flet import Container, Column, Text, TextButton, Stack


def create_second_page_content(page):
    return Container(
        content=Column(
            controls=[
                Stack(
                    controls=[
                        Text(value="Second Page"),
                        TextButton('go home', on_click=lambda _: page.go('/'))
                    ]
                )
            ],
        ),
    )
