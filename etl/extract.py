# Módulo de extração de dados

def extract_data(source):
    """
    Função para extrair dados de uma fonte específica.
    :param source: Localização da fonte de dados
    :return: Dados extraídos
    """
    # Exemplo de extração de dados
    if source == 'api':
        data = extract_from_api()
    elif source == 'database':
        data = extract_from_database()
    elif source == 'file':
        data = extract_from_file()
    else:
        raise ValueError("Fonte de dados desconhecida.")

    return data


def extract_from_api():
    # Lógica de extração de uma API
    data = {"name": "example", "value": 42}
    return data


def extract_from_database():
    # Lógica de extração de um banco de dados
    data = {"name": "example", "value": 42}
    return data


def extract_from_file():
    # Lógica de extração de um arquivo
    data = {"name": "example", "value": 42}
    return data