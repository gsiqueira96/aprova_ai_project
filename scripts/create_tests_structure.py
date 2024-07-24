import os

# Estrutura desejada para o diretório tests
tests_structure = [
    "tests/__init__.py",
    "tests/test_agent.py",
    "tests/test_etl.py",
    "tests/test_scraper.py"
]

# Função para criar diretórios e arquivos
def create_tests_structure(base_path="."):
    for path in tests_structure:
        full_path = os.path.join(base_path, path)
        if not os.path.exists(full_path):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                pass  # Cria arquivos vazios

# Executar a função para criar a estrutura tests
create_tests_structure()

print("Diretório 'tests' e arquivos criados com sucesso!")