import os

# Estrutura desejada para o diretório webscraping
webscraping_structure = [
    "webscraping/__init__.py",
    "webscraping/parser.py",
    "webscraping/scraper.py"
]

# Função para criar diretórios e arquivos
def create_webscraping_structure(base_path="."):
    for path in webscraping_structure:
        full_path = os.path.join(base_path, path)
        if not os.path.exists(full_path):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                pass  # Cria arquivos vazios

# Executar a função para criar a estrutura webscraping
create_webscraping_structure()

print("Diretório 'webscraping' e arquivos criados com sucesso!")