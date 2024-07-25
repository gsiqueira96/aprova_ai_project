import os

# Estrutura remanescente do projeto
remaining_structure = [
    "data/processed/",
    "data/raw/",
    "docs/README.md",
    "notebooks/exploratory_analysis.ipynb",
    "requirements.in",
    "setup.py",
    ".gitignore"
]

# Função para criar diretórios e arquivos
def create_remaining_structure(base_path="."):
    for path in remaining_structure:
        full_path = os.path.join(base_path, path)
        if path.endswith('/'):
            os.makedirs(full_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                pass  # Cria arquivos vazios

# Executar a função para criar a estrutura remanescente
create_remaining_structure()

print("Diretórios e arquivos remanescentes criados com sucesso!")