from processamento_dados import Dados

# Definindo caminhos:

path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

dados_empresa_a = Dados.leitura_dados(path_json, 'json')
dados_empresa_b = Dados.leitura_dados(path_csv, 'csv')

print(f"Nome das colunas da empresa A: {dados_empresa_a.nome_colunas}\n")
print(f"Quantidade de registros da empresa A: {dados_empresa_a.qtd_linhas}\n")

key_mapping = {"Nome do Item" : "Nome do Produto",
                "Classificação do Produto" : "Categoria do Produto",
                "Valor em Reais (R$)" : "Preço do Produto (R$)",
                "Quantidade em Estoque" : "Quantidade em Estoque" ,
                "Nome da Loja" : "Filial",
                "Data da Venda" : "Data da Venda"}

print(f"Nome das colunas da empresa B: {dados_empresa_b.nome_colunas}\n")
print(f"Quantidade de registros da empresa B: {dados_empresa_b.qtd_linhas}\n")
print(f"RENOMEANDO COLUNAS: {dados_empresa_b.renomear_colunas(key_mapping)}\n")
print(f"Nome das colunas da empresa B (PÓS): {dados_empresa_b.nome_colunas}\n")

dados_consolidados = Dados.juntar_dados(dados_empresa_a, dados_empresa_b)
print(f"Dados consolidados: {dados_consolidados}")

print(f"Nome das colunas dos dados consolidados: {dados_consolidados.nome_colunas}\n")
print(f"Quantidade de registros dos dados consolidados: {dados_consolidados.qtd_linhas}\n")

path_dados_consolidados = '../data_processed/dados_consolidados.csv2.csv'
dados_consolidados.salvar_dados(path_dados_consolidados)
print(path_dados_consolidados)
