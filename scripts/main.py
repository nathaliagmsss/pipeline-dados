from scripts.processamento_dados import Dados


def main():
    path_json = '../data_raw/dados_empresaA.json'
    path_csv = '../data_raw/dados_empresaB.csv'
    path_saida = '../data_processed/dados_consolidados.csv'

    # Leitura dos dados
    dados_empresa_a = Dados.leitura_dados(path_json, 'json')
    dados_empresa_b = Dados.leitura_dados(path_csv, 'csv')

    print(f"[Empresa A] Colunas: {dados_empresa_a.nome_colunas}")
    print(f"[Empresa A] Registros: {dados_empresa_a.qtd_linhas}\n")

    print(f"[Empresa B] Colunas: {dados_empresa_b.nome_colunas}")
    print(f"[Empresa B] Registros: {dados_empresa_b.qtd_linhas}\n")

    mapeamento = {"Nome do Item": "Nome do Produto",
                   "Classificação do Produto": "Categoria do Produto",
                   "Valor em Reais (R$)": "Preço do Produto (R$)",
                   "Quantidade em Estoque": "Quantidade em Estoque",
                   "Nome da Loja": "Filial",
                   "Data da Venda": "Data da Venda"}

    # Renomeando as colunas dos dados B
    dados_empresa_b.renomear_colunas(mapeamento)

    print(f"[Empresa B] Colunas após renomear: {dados_empresa_b.nome_colunas}\n")

    # Juntando dados A e dados B
    dados_consolidados = Dados.juntar_dados(dados_empresa_b, dados_empresa_a)

    print(f"[Consolidado] Colunas {dados_consolidados.nome_colunas}:")
    print(f"[Consolidado] Total de registros (esperado 4446): {dados_consolidados.qtd_linhas}\n")

    #Salvando os dados consolidados (A + B)
    dados_consolidados.salvar_dados(path_saida)
    print(f"Arquivo salvo com sucesso em: {path_saida}\n")

if __name__ == "__main__":
    main()
