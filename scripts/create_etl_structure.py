import os

# Estrutura desejada para o diretório etl
etl_structure = [
    "etl/__init__.py",
    "etl/extract.py",
    "etl/load.py",
    "etl/transform.py"
]

# Função para criar diretórios e arquivos
def create_etl_structure(base_path="."):
    for path in etl_structure:
        full_path = os.path.join(base_path, path)
        if not os.path.exists(full_path):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                pass  # Cria arquivos vazios

# Executar a função para criar a estrutura etl
create_etl_structure()

print("Diretório 'etl' e arquivos criados com sucesso!")