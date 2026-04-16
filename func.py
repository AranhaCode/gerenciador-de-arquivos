from pathlib import Path
from datetime import datetime
import os
import shutil
from PIL import Image
from dados import tipos_arquivos
def menu():
        print("="*40)
        print("MENU")
        print("="*40)
        escolha_do_menu= input("Escolha oque deseja fazer:  \n1.Criar arquivo \n2.Mover arquivos  \n3.Deletar arquivos  \n 4.Visualizar \n5.Sair")
        return escolha_do_menu
def criar():
        agora_para_pdf_jpg_png = datetime.now()
        os.makedirs("Backup" , exist_ok=True)
        escolha_de_criar_arquivo= input("Qual tipo de arquivo deseja criar?:  \n1.Pdf  \n2.Jpg  \n3.Png  \n4.Word ")
        match escolha_de_criar_arquivo:
                        case "1": 
                                os.makedirs("Pdfs", exist_ok=True)
                                nome_aplicado_para_pdf = input("Insira o nome que deseja dar ao arquivo:").lower()
                                conteudo_aplicado_dentro_pdf = input("Insira oque voce deseja colocar nele:")
                                try:
                                        with open(f"Pdfs/{nome_aplicado_para_pdf}__{agora_para_pdf_jpg_png:%d-%m-%Y_%H-%M}.pdf", "a" , encoding="utf-8") as arquviopdf:
                                                arquviopdf.write(conteudo_aplicado_dentro_pdf + "\n")
                                                print(f"O arquivo {nome_aplicado_para_pdf} foi criado")
                                                shutil.copy2("Pdfs" , "Backup" , dirs_exist_ok=True)
                                except Exception as e:
                                                   print(f"Ops ocorreu um erro: {e}")
                        case "2":
                                os.makedirs("Imagens", exist_ok=True)
                                nome_aplicado_para_jpg = input("Insira o nome que deseja dar ao arquivo:").lower()
                                conteudo_aplicado_dentro_jpg = input("Arraste a imagem para aqui:").strip().replace('& ', '').replace('"', '').replace("'", "")
                                agora_para_jpg = datetime.now().strftime("%d-%m-%Y_%H-%M")
                                try:
                                   foto_jpg = Image.open(conteudo_aplicado_dentro_jpg)
                                   foto_colorida = foto_jpg.convert("RGB")
                                   final_jpg = f"Imagens/{nome_aplicado_para_jpg}_{agora_para_jpg}.jpg"
                                   foto_colorida.save(final_jpg , "JPEG")
                                   print(f"A imagem {nome_aplicado_para_jpg} foi salva")
                                   shutil.copy2("Imagens" , "Backup" , dirs_exist_ok=True)


                                except Exception as e:
                                                 print(f"Ops ocorreu algum erro: {e}")
                        case "3":
                                os.makedirs("Imagens", exist_ok=True)
                                nome_aplicado_para_png= input("Insira o nome que deseja dar ao arquivo:").lower()
                                conteudo_aplicado_dentro_png= input("Arraste a imagem para aqui:").strip().replace('& ', '').replace('"', '').replace("'", "")
                                agora_para_png = datetime.now().strftime("%d-%m-%Y_%H-%M")
                                try:
                                   foto_png = Image.open(conteudo_aplicado_dentro_png)
                                   final_png = f"Imagens/{nome_aplicado_para_png}_{agora_para_png}.png"
                                   foto_png.save(final_png, "PNG")
                                   print(f"A imagem {nome_aplicado_para_png} foi salva")
                                   shutil.copy2("Imagens" , "Backup" , dirs_exist_ok=True)
                                except Exception as e:
                                                 print(f"Ops ocorreu algum erro: {e}")
                        case "4":
                                os.makedirs("Words", exist_ok=True)
                                nome_aplicado_para_word = input("Insira o nome que deseja dar ao arquivo:").lower()
                                conteudo_aplicado_dentro_jpg = input("Insira oque voce deseja colocar nele:")
                                try:
                                        with open(f"Words/{nome_aplicado_para_word}__{agora_para_pdf_jpg_png:%d-%m-%Y_%H-%M}.docx", "a" , encoding="utf-8") as arquvioword:
                                                arquvioword.write(conteudo_aplicado_dentro_jpg + "\n")
                                                shutil.copy2("Words" , "Backup" , dirs_exist_ok=True)
                                                print(f"O arquivo {nome_aplicado_para_word} foi criado")  
                                                
                                               
                                except Exception as e:
                                        print(f"Ops ocorreu algum erro: {e}")                                    
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
                        print(f"Ops ouve algum erro: {e}")
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
                                print(f"Ops ouve algum erro: {e}")
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

        

