import json
import csv
from processamento_dados import Dados

path_json = "data_raw/dados_empresaA.json"
path_csv = "data_raw/dados_empresaB.csv"

#Extração

dados_empresa_A = Dados(path_json, "json")
print("Empresa A: ", dados_empresa_A.nome_colunas)

dados_empresa_B = Dados(path_csv, "csv")
print("Empresa B: " , dados_empresa_B.nome_colunas)

# #Transformação dos dados

key_map = {'Nome do Item':'Nome do Produto',       
            'Classificação do Produto':'Categoria do Produto',
            'Valor em Reais (R$)':'Preço do Produto (R$)',
            'Quantidade em Estoque':'Quantidade em Estoque',
            'Nome da Loja':'Filial',
            'Data da Venda':'Data da Venda'}

dados_empresa_B.renomea_colunas(key_map)

print("Empresa B novo: " , dados_empresa_B.nome_colunas)

dados_fusao = Dados.join(dados_empresa_A, dados_empresa_B)

print("Dados fusão nome das colunas: ", dados_fusao.nome_colunas)
print("Dados fusão quantidade de linhas: ", dados_fusao.qtd_linhas)

#Load
caminho_dados_combinados = "data_processed/dados.combinados.csv"
dados_fusao.salvando_dados(caminho_dados_combinados)
print(caminho_dados_combinados)