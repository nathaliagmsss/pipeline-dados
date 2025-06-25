import csv
import json

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__ler_colunas()
        self.qtd_linhas = self.__size_data()

    @staticmethod
    def __leitura_json(path):
        dados_json = []
        with open(path, 'r', encoding='utf-8') as file:
            dados_json = json.load(file)
        return dados_json

    @staticmethod
    def __leitura_csv(path):
        dados_csv = []

        with open(path, 'r', encoding='utf-8') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def leitura_dados(cls, path, type_data):
        dados = []

        if type_data == 'json':
            dados = cls.__leitura_json(path)
        elif type_data == 'csv':
            dados = cls.__leitura_csv(path)
        else:
            return "Formato invalido"
        return cls(dados)

    def __ler_colunas(self):
        colunas = list(self.dados[0].keys())
        return colunas

    def renomear_colunas(self, key_mapping):
        new_dados = []

        for item in self.dados:
            dict_temp = {}
            for old_key, value in item.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)

        self.dados = new_dados
        self.nome_colunas = self.__ler_colunas()

    def __size_data(self):
        return len(self.dados)

    @staticmethod
    def juntar_dados(dados_a, dados_b):
        return Dados(dados_a.dados + dados_b.dados)

    def __transformar_para_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela  #retorna lista de listas

    def salvar_dados(self, path):
        dados_combinados_tabela = self.__transformar_para_tabela()

        with open(path, 'w', newline='', encoding='utf-8') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(dados_combinados_tabela)