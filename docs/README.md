# Aprova AI Project

## Visão Geral

O Aprova AI Project é uma iniciativa para desenvolver um sistema de automação e inteligência artificial capaz de realizar tarefas de ETL (Extração, Transformação e Carga de Dados), web scraping, processamento de dados e orquestração de agentes autônomos usando a framework CrewAI.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
aprova_ai_project/
├── aprova_crew/
│   ├── README.md
│   ├── pyproject.toml
│   ├── src/
│   │   └── aprova_crew/
│   │       ├── __init__.py
│   │       ├── config/
│   │       │   ├── agents.yaml
│   │       │   └── tasks.yaml
│   │       ├── crew.py
│   │       ├── main.py
│   │       └── tools/
│   │           ├── __init__.py
│   │           └── custom_tool.py
│   └── tests/
├── data/
│   ├── processed/
│   └── raw/
├── docs/
│   └── README.md
├── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── load.py
│   └── transform.py
├── main.py
├── notebooks/
│   └── exploratory_analysis.ipynb
├── requirements.txt
├── scripts/
│   ├── create_etl_structure.py
│   ├── create_tests_structure.py
│   ├── create_utils_structure.py
│   ├── create_ws_structure.py
│   └── remanescente_structure.py
├── settings.py
├── setup.py
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_etl.py
│   └── test_scraper.py
├── utils/
│   ├── __init__.py
│   ├── data_processing.py
│   └── helpers.py
└── webscraping/
    ├── __init__.py
    ├── parser.py
    └── scraper.py
```

## Instalação

Para instalar as dependências necessárias, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## Configuração

Certifique-se de definir suas variáveis de ambiente no arquivo `.env` para integrar com a API do CrewAI:

```
CREWAI_API_KEY=your-default-api-key
```

## Uso

Para iniciar o projeto, você pode executar o script principal:

```bash
python main.py
```

## Funcionalidades

- **ETL (Extração, Transformação e Carga de Dados):** Scripts localizados na pasta `etl` para realizar tarefas de ETL.
- **Web Scraping:** Scripts localizados na pasta `webscraping` para coleta de dados da web.
- **Processamento de Dados:** Funções utilitárias na pasta `utils` para manipulação e processamento de dados.
- **Orquestração de Agentes Autônomos:** Usando a framework CrewAI, localizado na pasta `aprova_crew`.

## Testes

Para rodar os testes, use o comando:

```bash
pytest
```

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests. Todas as contribuições são bem-vindas!

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para mais informações, entre em contato com o autor:
- Gabriel Siqueira: rushcompany777@gmail.com

---

Esperamos que este README forneça uma visão clara e concisa do projeto Aprova AI. Boa codificação!
```