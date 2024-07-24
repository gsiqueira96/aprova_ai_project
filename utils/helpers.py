import os


def create_directory(path):
    """Criar um diretório se ele não existir"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Diretório criado: {path}")
    else:
        print(f"Diretório já existe: {path}")


def save_to_file(data, file_path):
    """Salvar dados em um arquivo"""
    try:
        with open(file_path, "w") as file:
            file.write(data)
        print(f"Dados salvos em: {file_path}")
    except IOError as e:
        print(f"Erro ao salvar dados: {e}")


def read_from_file(file_path):
    """Ler dados de um arquivo"""
    try:
        with open(file_path, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None
