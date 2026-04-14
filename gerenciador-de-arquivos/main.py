from datetime import datetime
from func import menu , criar , movera , deletar , visualizar

while True:
    escolha_do_menu_principal = menu()
    match escolha_do_menu_principal:
        case "1":
            print("Indo para criaçao de arquivos")
            criar()
        case "2":
            print("Indo para a parte de mover arquivos")
            movera()
        case "3":
            print("Indo para remoçao de arquivos")
            deletar()
        case "4":
            print("Indo para a visualizaçao de arquivos")
            visualizar()
        case "5":
            print("Encerrando sistema")
            break
