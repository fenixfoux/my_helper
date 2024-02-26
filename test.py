import flet as ft

def main(page: ft.Page):
    # Поле для ввода
    text_input = ft.TextField()


    # Функция для создания нового поля с введенным текстом
    def save_text(e):
        # Получение текста из поля ввода
        text = text_input.value

        # Создание нового текстового поля
        new_text_field = ft.Text(text)

        # Добавление нового текстового поля на страницу
        page.add(new_text_field)

    # Кнопка "Сохранить"
    save_button = ft.ElevatedButton(text="Сохранить", on_click=save_text)

    # Отображение элементов на странице
    page.add(text_input)
    page.add(save_button)

ft.app(target=main)
