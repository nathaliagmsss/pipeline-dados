# 📊 Pipeline de Dados - Consolidação de Arquivos CSV e JSON

Este projeto demonstra uma etapa fundamental de Engenharia de Dados: a **extração, transformação e consolidação** de dados oriundos de diferentes fontes (CSV e JSON), utilizando Python puro.

O projeto foi desenvolvido como parte de um curso da Alura e tem como objetivo a consolidação de dados de duas empresas, gerando um arquivo único de saída.

---

## 🧠 Funcionalidades

- Leitura de arquivos `.json` e `.csv` em formato de dicionário.
- Renomeação automática de colunas para padronização.
- Junção dos dados em uma única estrutura consolidada.
- Salvamento do resultado em um novo arquivo `.csv`.
- Estrutura de código reutilizável e orientada a objetos.

---

## 📁 Estrutura do Projeto

```
pipeline-py-dados/
├── data_raw/                    # Dados brutos (entrada)
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
│
├── data_processed/              # Dados processados (saída)
│   └── dados_consolidados.csv
│
├── scripts/                    # Lógica e execução
│   ├── processamento_dados.py  # Classe Dados (ETL)
│   └── main.py                 # Script principal de execução
│
├── README.md                   # Documentação do projeto
└── .gitignore                  # Arquivos a ignorar no Git
```


---

## 🚀 Como Executar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/scripts
```

2. Certifique-se de você tem o Python 3 baixado
   
3. Execute o Script principal:

```
python main.py
``` 

4. O resultado será salvo na pasta data_processed/ com o nome dados_consolidados.csv.

---

## 🔧 Requisitos

Python 3.7+

Nenhuma biblioteca externa é necessária (somente csv e json da biblioteca padrão).

## 🧪 Exemplo de Uso

Suponha que os dados da empresa A venham em JSON e os da empresa B em CSV, com diferentes nomes de colunas. O script renomeia, junta e salva tudo padronizado. Ideal para aplicações reais de pré-processamento de dados.

## ✍️ Autora

**Nathália Gomes**  
[LinkedIn](https://www.linkedin.com/in/nathaliagomes)

Projeto criado como parte dos estudos em Engenharia de Dados.
