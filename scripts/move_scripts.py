import os
import shutil

# Diretório scripts e arquivos a serem movidos
scripts_directory = "scripts"
files_to_move = [
    "create_etl_structure.py",
    "create_tests_structure.py",
    "create_utils_structure.py",
    "create_ws_structure.py",
    "remanescente_structure.py"
]

# Função para criar o diretório scripts e mover os arquivos
def create_scripts_directory_and_move_files():
    if not os.path.exists(scripts_directory):
        os.makedirs(scripts_directory)
        print(f"Diretório '{scripts_directory}' criado com sucesso!")

    for file in files_to_move:
        if os.path.exists(file):
            shutil.move(file, os.path.join(scripts_directory, file))
            print(f"Arquivo '{file}' movido para '{scripts_directory}' com sucesso!")

# Executar a função para criar o diretório scripts e mover os arquivos
create_scripts_directory_and_move_files()

print("Diretório 'scripts' criado e arquivos movidos com sucesso!")