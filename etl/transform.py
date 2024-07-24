# Módulo de transformação de dados

def transform_data(data):
    """
    Função para transformar dados extraídos.
    :param data: Dados extraídos
    :return: Dados transformados
    """
    # Exemplo de transformação de dados
    transformed_data = {}

    for key, value in data.items():
        transformed_data[key.upper()] = value * 2

    return transformed_data