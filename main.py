import flet as ft

# Formulário - Nome, sobrenome, E-mail e senha.

def main(page: ft.Page):
    width_padrao = 300
    
    pais = input("Digite o número do seu país: " + " ")
    ddd = input("Digite o número do seu país: " + " ")
    
    name = ft.TextField(label = "Nome", value = "", width = width_padrao)
    second_name = ft.TextField(label = "Sobrenome", value = "", width = width_padrao)
    email = ft.TextField(label = "Email", value = "", width = width_padrao)
    tel = ft.TextField(label = "Telefone", value = "", prefix_text=pais + " " + ddd + " " + "9", width = width_padrao, input_filter = ft.NumbersOnlyInputFilter())
    password = ft.TextField(label = "Senha", password = True, can_reveal_password = True, value = "", width = width_padrao)
    
    page.add(
        ft.Column(controls=[
            name,
            second_name,
            email,
            tel,
            password
        ])
    )
    # name_value = 
ft.app(main)