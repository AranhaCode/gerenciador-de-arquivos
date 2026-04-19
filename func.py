from pathlib import Path
from datetime import datetime
import os
import shutil
from PIL import Image
from dados import tipos_arquivos
import random
def menu():
        print("="*40)
        print("MENU")
        print("="*40)
        escolha_do_menu= input("Escolha oque deseja fazer:  \n1.Criar arquivo \n2.Mover arquivos  \n3.Deletar arquivos  \n 4.Visualizar \n5.Sair")
        return escolha_do_menu
def criar():
        os.makedirs("Pdfs", exist_ok=True)
        os.makedirs("Imagens", exist_ok=True)
        os.makedirs("Imagens", exist_ok=True)
        os.makedirs("Words", exist_ok=True)
        os.makedirs("Backup" , exist_ok=True)
        escolha_de_criar_arquivo= input("Qual tipo de arquivo deseja criar?:  \n1.Pdf  \n2.Jpg  \n3.Png  \n4.Word ")
        nome_aplicado_aos_arquivos = input("Insira o nome que deseja dar ao arquivo:").lower()
        agora = datetime.now().strftime("%d-%m-%Y_%H-%M")
        try:
                match escolha_de_criar_arquivo:
                        case "1": 
                                conteudo_pdf = input("Insira o que deseja colocar nele: ")
                                caminho_final = f"Pdfs/{nome_aplicado_aos_arquivos}__{agora}.pdf"
                                with open(caminho_final, "a", encoding="utf-8") as arquivo:
                                        arquivo.write(conteudo_pdf + "\n")

                        case "2" | "3":
                                conteudo_img = limpar_caminho(input("Arraste a imagem para aqui: "))
                                extensao = "jpg" if escolha_de_criar_arquivo == "2" else "png"
                                caminho_final = f"Imagens/{nome_aplicado_aos_arquivos}_{agora}.{extensao}"
                                with Image.open(conteudo_img) as Foto_convertida:
                                        if escolha_de_criar_arquivo == "2":
                                                Foto_convertida = Foto_convertida.convert("RGB")
                                        Foto_convertida.save(caminho_final)

                        case "4":
                                conteudo_word = input("Insira o que deseja colocar nele: ")
                                caminho_final = f"Words/{nome_aplicado_aos_arquivos}__{agora}.docx"
                                with open(caminho_final, "a", encoding="utf-8") as arquivo:
                                        arquivo.write(conteudo_word + "\n")
                        case _:
                                print("Opção inválida")
                                return 
                print(f" O arquivo '{nome_aplicado_aos_arquivos}' foi criado!")
                salvar_e_backup(os.path.dirname(caminho_final), caminho_final)
        except Exception as e:
                print(f"Ops ocorreu um erro: {e}")

                
                                                        
        except Exception as e:
                print(f"Ops houve algum erro: {e}")          
def movera():
        escolha_mover_arquivo = input("Qual tipo de arquivo voce deseja mover?: \n1.Pdf  \n2.Jpg  \n3.Png  \n4.Word")
        if escolha_mover_arquivo in tipos_arquivos:
                arquivo_mover = input("Escreva o nome do arquivo ou arraste ele para ca").lower().strip().replace('& ', '').replace('"', '').replace("'", "")
                escolher_o_destino = input("Escreva o nome da pasta que deseja mover o arquivo")
                try:
                        if os.path.exists(arquivo_mover) and os.path.exists(escolher_o_destino):
                                shutil.move(arquivo_mover , escolher_o_destino)
                                print(f"O {arquivo_mover} foi movido para {escolher_o_destino}")
                        else:
                                print("O arquivo nao foi encontrado")
                except Exception as e:
                        print(f"Ops houve algum erro: {e}")
        else:
                print("O arquivo nao existe ou pasta nao existe")                
def deletar():
        escolha_deletar_arquivo = input("Qual tipo de arquivo deseja deletar?:  \n1.Pdf  \n2.Jpg  \n3.Png  \n4.Word ")
        match escolha_deletar_arquivo:
                case "1" | "2" | "3" | "4":
                        deletar_arquivo= input("Insira o nome do arquivo completo ou arraste ele para ca").lower().strip().replace('& ', '').replace('"', '').replace("'", "")
                        try:
                                if os.path.exists(deletar_arquivo): 
                                        os.remove(deletar_arquivo)
                                        print(f"O arquivo {deletar_arquivo} foi removido ")
                                else:
                                        print(f"O arquivo na foi encontrado")
                        except Exception as e:
                                print(f"Ops houve algum erro: {e}")
def visualizar():
        escolha_visualizar = input("Digite a pasta que voce deseja visualizar:")
        if os.path.exists(escolha_visualizar):
                try:
                        conteudo_arquivo = os.listdir(escolha_visualizar)
                        
                        if conteudo_arquivo:
                           print(f"\nConteúdo de '{escolha_visualizar}':\n")
                           for item in conteudo_arquivo:
                                        conteudo_arquivo_completo = os.path.join(escolha_visualizar, item)
                                        if os.path.isdir(conteudo_arquivo_completo):
                                         print(f"[PASTA] {item}")
                                        else:
                                         print(f"[ARQUIVO] {item}")
                        else:
                          print(f"A pasta '{escolha_visualizar}' está vazia!")
                          
                except Exception as e:
                        print(f"Erro ao listar conteúdo: {e}")
        else:
             print("A pasta não foi encontrada!")
def limpar_caminho(caminho):
    for caractere in ['& ', '"', "'"]:
        caminho = caminho.replace(caractere, '')
    return caminho.strip()
def salvar_e_backup(arquivo_origem):
    os.makedirs("Backup", exist_ok=True)
    shutil.copy2(arquivo_origem, "Backup")
def login():
        tentativas = 0
        os.makedirs("Senha e usuario", exist_ok=True)
        caminho_usuario = "Senha e usuario/usuario.txt"
        caminho_senha = "Senha e usuario/senha.txt"
        while tentativas < 3:
                perguntando_usuario_login = input("Voce possui um login?: [S/N]").lower()
                if not os.path.exists(caminho_usuario):
                        with open(caminho_usuario, "w") as f: pass
                        with open(caminho_senha, "w") as f: pass
                try:
                                if perguntando_usuario_login == "s":
                                        insirir_usuario = input("Insira seu nome de usuario:")
                                        insirir_senha = input("Insira sua senha:")
                                        with open(caminho_usuario , "r") as arquivo_usuario:
                                                conteudo_usuario = arquivo_usuario.read().splitlines()
                                        with open(caminho_senha , "r") as arquivo_senha:
                                                conteudo_senha = arquivo_senha.read().splitlines()
                                        if insirir_usuario in conteudo_usuario:
                                                posicao = conteudo_usuario.index(insirir_usuario)
                                                if insirir_senha == conteudo_senha[posicao]:
                                                        print("Acesso liberado")
                                                        print(f"Seja bem vindo {insirir_usuario}")
                                                        return True
                                                else:   
                                                 print("Senha ou usuario incorretos")
                                                 tentativas += 1
                                        else:
                                                print("Usuario nao encontrado")
                                                tentativas += 1
                                else:
                                        pergunta_criar_login = input("Voce deseja criar um login?: [S/N]").lower()
                                        if pergunta_criar_login == "s":
                                                criar_nome_usuario = input("Digite o nome de usuario que deseja ter:")
                                                if criar_nome_usuario == "":
                                                        print("Nome invalido")
                                                        continue
                                                criar_senha_usuario = input("Digite a senha que daseja ter ou aperte [1] para gerar uma senha aleatoria A senha deve conter apenas numeros!!!:")
                                                if criar_senha_usuario == "":
                                                        print("Senha invalida")
                                                        continue
                                                if criar_senha_usuario == "1":
                                                        criar_senha_usuario = str(random.randint(1000,10000))
                                                        
                                                with open(caminho_usuario , "a", encoding="utf-8") as arquivo:
                                                        arquivo.write(criar_nome_usuario + "\n")
                                                with open(caminho_senha , "a" , encoding="utf-8") as arquivo:
                                                        arquivo.write(criar_senha_usuario  + "\n")
                                                        print(f"Seu nome de usuario é {criar_nome_usuario} e sua senha é {criar_senha_usuario}")
                except Exception as e:
                        print(f"Ops houve algum erro: {e}")
                        break
        print("\nTentativas esgotadas. Fechando programa por segurança.")
        return False
             


                     

                     


        

