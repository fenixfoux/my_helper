# tab_names = {
#     'eng': {
#         'all': "all",
#         '0': 'active',
#         '1': 'completed'
#     },
#     'rus': {
#         'all': "все",
#         '0': 'в процессе',
#         '1': 'готово'
#     }
# }
# selected_lang = 'eng'
# gg = "active"
# print(tab_names[selected_lang])
# for elem in tab_names[selected_lang]:
#     # print(f"elem is '{elem}'") # get keys
#     # print(tab_names[selected_lang][elem])
#     if tab_names[selected_lang][elem] == gg:
#         print(f"tab_names[selected_lang][elem] == gg is {tab_names[selected_lang][elem] == gg}")
#         # print(tab_names[selected_lang][elem])
#         print(elem)
#
# import datetime
# today = datetime.date.today()
# print(today)

import flet as ft

name = "PieChart 3"


def example():
    normal_radius = 15

    def badge(icon, size):
        return ft.Container(
            ft.Icon(icon, size=size*0.75),
            width=size,
            height=size,
            border=ft.border.all(1, ft.colors.BROWN),
            border_radius=size / 2,
            bgcolor=ft.colors.WHITE,
        )

    chart = ft.PieChart(
        width=normal_radius,
        height=normal_radius,
        sections=[
            ft.PieChartSection(
                10,
                color=ft.colors.GREY,
                radius=normal_radius,
                # badge=badge(ft.icons.AC_UNIT, normal_badge_size),
                badge_position=0.98,
            ),
            ft.PieChartSection(
                90,
                color=ft.colors.GREEN,
                radius=normal_radius,
                badge=badge(ft.icons.AC_UNIT, normal_radius/2*1.5),
                badge_position=0,
            ),
        ],
        sections_space=0,
        center_space_radius=0,
        expand=True,
    )

    return chart

def main(page: ft.Page):
    page.add(example())


# if __name__ == "__main__":
#     ft.app(target=main)

