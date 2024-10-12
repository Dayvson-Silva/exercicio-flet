# import flet as ft

# def main(page: ft.page):
#     page.title= "Treinando Flet"
#     hello = ft.Text(value="Hello World!" , size=100 )
#     page.controls.append(hello)
#     page.update()
#     page.add(
#         ft.ElevatedButton("Clique aqui", on_click=lambda _ : page.add(ft.Text("Bora Biuuuuuuuuuuuuuu")) ))
    
# ft.app(target=main)

# def main1(page: ft.page):
#     page.title = "Biu"
    
#     layout = ft.Column(
#         controls=[
#             ft.Text("Botões do Biu" , size=100 , weight=ft.FontWeight.BOLD),
#             ft.ElevatedButton("Bora Biu" , on_click=lambda _:page.add(ft.Text("Boraaa Biuuuuuu"))),
#             ft.ElevatedButton("Bora fiii do Biu",on_click=lambda _:page.add(ft.Text("Boraaa Fiii Biuuuuuu"))),
#             ft.ElevatedButton("Bora Mulher do Biu",on_click=lambda _:page.add(ft.Text("Boraaa Mulher do Biu")))
         
#         ]
#     )
    
#     page.add(layout)

# ft.app(target=main1)

# import flet as ft

# def main(page):
#     def add_clicked(e):
#         page.add(ft.Checkbox(label=new_task.value))
#         new_task.value = ""
#         new_task.focus()
#         new_task.update()

#     new_task = ft.TextField(hint_text="Escreve tua Lista BB", width=300)
#     page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

# ft.app(main)

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.AutofillGroup(
            ft.Column(
                controls=[
                    
                    
                    ft.TextField(
                        label="Nome",value="",
                        autofill_hints=ft.AutofillHint.NAME, 
                    ),
                    ft.TextField(
                        label="Sobrenome",value="",
                        autofill_hints=ft.AutofillHint.NAME,
                    ),
                    ft.TextField(
                        label="Email",value="",
                        autofill_hints=[ft.AutofillHint.EMAIL],
                    ),
                    ft.TextField(
                        label="Telefone",value="", prefix_text= "+55 ", input_filter=ft.NumbersOnlyInputFilter() ,
                        autofill_hints=[ft.AutofillHint.TELEPHONE_NUMBER],
                    ),
                    ft.TextField(
                        label="Endereço",value="",
                        autofill_hints=ft.AutofillHint.FULL_STREET_ADDRESS,
                    ),
                    ft.TextField(
                        label="Senha",value="",
                        autofill_hints=ft.AutofillHint.FULL_STREET_ADDRESS,password=True,can_reveal_password=True
                    ),
               
                     ft.ElevatedButton(text="Enviar Fórmulario", on_click=lambda _ : page.add(ft.Text("Enviado Com Sucesso")),color="green", ),
                                  
                ]
            )
        )
    )


ft.app(main)