import flet as ft


def example():
    def open_dlg_modal(e):
        e.control.page.dialog = dlg_modal
        dlg_modal.open = True
        e.control.page.update()

    def close_dlg(e):
        dlg_modal.open = False
        e.control.page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        # content=ft.TextField(key='any_key_name', value="Do youiles?"), # with key don't work properly
        content=ft.TextField(value="Do youiles?"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    return ft.Column(
        [
            ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
        ]
    )


def main(page):
    page.title = "Card Example"
    page.add(
        example()
    )


ft.app(target=main)
