# AutoText
# Preenchedor de textos prontos
# Autor: Tom-Dev-Full
# 2023

import os.path as path
import os

def existe(nome):
  #VERIFICA A EXISTÊNCIA DO ARQUIVO
  if(path.isfile(f"Textos/{nome}.rtf")):
    return True
  else:
    return False

# 1. SELECIONAR E COLAR TEXTO

  # 1.1 ABRIR ARQUIVO COM O TEXTO
def colar(nome):
   if(existe(nome)):
    with open(f"Textos/{nome}.rtf","r") as arquivo:
   # 1.2 COLAR TEXTO
      print(arquivo.read())
  # 1.3  SALVAR EM RECENTES
      recente(nome)
   else:
     print("Arquivo não encontrado")
     
#colar(input("\nQual arquivo deseja colar?\n"))   

# 2. GERENCIAR TEXTOS
  # 2.1 CRIAR TEXTO
    # 2.1.1 CRIAR ARQUIVO ACRESCENTAR TEXTO
    # 2.1.2 VERIFICAR SE JÁ EXISTE
def criar(nome,texto):

  if(existe(nome)):
    print("\nO arquivo já existe.\n")
      
  else:
    with open(f"Textos/{nome}.rtf","w+") as arquivo:
      arquivo.write(texto)  
    
    # 2.1.3 SELECIONAR TIPO *
    # 2.1.4 ORGANIZAR TEXTOS POR TIPOS (E-MAIL, SAJ, WORD, ETC.) *

# 2.2 EDITAR TEXTO
    # 2.2.1 COLAR TEXTO EM UMA VARIÁVEL, EDITÁ-LO, ABRIR O RESPECTIVO ARQUIVO E SUBSTITUIR O TEXTO
def editar(nome):
   if(existe(nome)):
     with open(f"Textos/{nome}.rtf","r") as arquivo:
      temp = arquivo.read()

      sub = input(f"O texto atual é: {temp} \n\nDigite o novo texto:\n")

      with open(f"Textos/{nome}.rtf","w") as arquivo2:
        arquivo2.write(sub)  
   else:
     print("\nArquivo não existe!")

 
  # 2.3 EXCLUIR TEXTO
    # 2.3.1 APAGAR ARQUIVO
def excluir(arquivo):
   if(existe(arquivo)):
     os.remove(f"Textos/{arquivo}.rtf")
     print("A\nrquivo exluido!")
   else:
     print("\nArquivo não existe.")

# 3. MOSTRAR RECENTES
  
  # 3.1 SALVAR O NOME DOS ÚLTMIMOS TEXTOS EM UMA LISTA OU ARQUIVO
    # 3.1.1 SUBSTITUIR O PRIMEIRO PELO ANTECESSOR
global recentes
recentes = []
#*** simplificar função
def recente(nome):
  
  if(len(recentes) <= 4):
    #VERIFICA SE A QUANTIDADE É =>5
    if(recentes.count(nome) == 0):
      
      recentes.insert(0,nome)
    else:
      recentes.remove(nome)
      recentes.insert(0,nome)
       
      
  else:
    
    if(recentes.count(nome) == 0):
      #VERIFICA SE NÃO EXISTE
      recentes.pop(4)
      recentes.insert(0,nome)
    else:
      recentes.remove(nome)
      recentes.insert(0,nome)  
    
  
       
  
def mostrar():
  print(recentes)
  
  # 3.2 SELECIONAR O TEXTO DE ACORDO COM O NOME

# 4. APRESENTAR AS OPÇÕES DE TEXTOS

#INTERAÇÃO PROVISÓRIA, SUBSTITUIR POR GUI
def pergunta():
  print("\nOpções:\n\n1) Criar\n\n2) Editar\n\n3) Excluir\n\n4) Colar\n\n5) Mostrar recentes\n\n6) Fim\n")
  global resposta
  resposta = input()

pergunta()

while resposta != "Fim":
  
  match resposta:
    case '1':
      criar(input("Nome do arquivo: "),input("Texto: "))
      pergunta()
    case '2':
      editar(input("Nome do arquivo: "))
      pergunta()
    case '3':
      excluir(input("Nome do arquivo: "))
      pergunta()
    case '4':
      colar(input("Nome do arquivo: "))
      pergunta()
    case '5':
      mostrar()
      pergunta()  
    case '6':
      resposta = "Fim"

