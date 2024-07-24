import os

# Estrutura desejada para o diretório utils
utils_structure = [
    "utils/__init__.py",
    "utils/data_processing.py",
    "utils/helpers.py"
]

# Função para criar diretórios e arquivos
def create_utils_structure(base_path="."):
    for path in utils_structure:
        full_path = os.path.join(base_path, path)
        if not os.path.exists(full_path):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                pass  # Cria arquivos vazios

# Executar a função para criar a estrutura utils
create_utils_structure()

print("Diretório 'utils' e arquivos criados com sucesso!")