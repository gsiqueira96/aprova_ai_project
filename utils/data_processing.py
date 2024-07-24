import pandas as pd


def load_data(file_path):
    """Carregar dados de um arquivo CSV"""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None


def clean_data(data):
    """Limpar e preparar dados"""
    data.dropna(inplace=True)
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
    return data


def transform_data(data):
    """Transformar dados para análise"""
    # Exemplo de transformação
    data["new_column"] = data["existing_column"].apply(lambda x: x * 2)
    return data
