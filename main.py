import main as ft

def main(page: ft.Page):
    hello = ft.Text(value = "Hello world!", size = 30)
    page.controls.append(hello)
    page.update()

ft.app(target=main)