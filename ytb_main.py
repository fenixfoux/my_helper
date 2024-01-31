from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    widget_color = 'white'

    # def shrink(e):
    #     page_2.controls[0].width = 120
    #     page_2.update()

    create_task_view = Container(
        content=Container(
            on_click= lambda _: page.go('/'),
            height=40, width=40,
            content=Text('x'))
    )



    tasks = Column(
        height=400, scroll='auto',
        controls=[
            # Container(height=50, width=300, bgcolor='red'),
            # Container(height=50, width=300, bgcolor='red'),
            # Container(height=50, width=300, bgcolor='red'),
        ]
    )
    for i in range(10):
        tasks.controls.append(
            Container(
                height=70, width=400, bgcolor='white12',
                border_radius=10,
                content=Checkbox(
                    label='some dummy task',
                )),)


    categories_card = Row(
        scroll='auto'
    )
    categories = ["Business", "Work", "Daily"]
    for category in categories:
        categories_card.controls.append(
            Container(
                bgcolor=BG, height=110, width=170,
                border_radius=20, padding=15,
                content=Column(
                    controls=[
                        Text('50 tasks', color=widget_color),
                        Text(category, color=widget_color),
                        Container(width=160, height=5,
                                  border_radius=20, bgcolor='white12',
                                  padding=padding.only(right=50),
                                  content=Container(bgcolor=PINK)
                                  )
                    ]
                )
            ))
    first_page_content = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            # on_click= lambda e: shrink(e),
                            content=Icon(icons.MENU, color=widget_color)),
                        Row(controls=[
                            Icon(icons.SEARCH, color=widget_color),
                            Icon(icons.NOTIFICATIONS_OUTLINED, color=widget_color)
                        ])
                    ]),
                Text(value="What\'s up, bro!", color=widget_color),
                Text(value="Categories", color=widget_color),
                Container(
                    padding=padding.only(top=20, bottom=20, ),
                    content=categories_card
                ),
                Text(value='Today\'s tasks', color=widget_color),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=2, right=20,
                            icon=icons.ADD, on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ],
        ),
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                # animate_scale=animation.Animation(400, curve='decelerate'),
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(
                    controls=[
                        first_page_content
                    ]
                )
            )
        ]
    )

    content_container = Container(
        width=400,
        height=850,
        bgcolor=FWG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )

    pages = {
        '/': View(
            "/",
            [content_container],
        ),
        '/create_task': View(
            "create_task",
            [create_task_view],
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    page.add(content_container)

    page.on_route_change = route_change
    page.go(page.route)


app(target=main)
