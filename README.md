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
└── .gitignore                  # (opcional) Arquivos a ignorar no Git
