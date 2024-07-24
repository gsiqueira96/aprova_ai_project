# Módulo de carga de dados

def load_data(data, destination):
    """
    Função para carregar dados transformados em um destino específico.
    :param data: Dados transformados
    :param destination: Localização do destino de dados
    :return: Confirmação de carga
    """
    # Exemplo de carga de dados
    if destination == 'database':
        load_to_database(data)
    elif destination == 'file':
        load_to_file(data)
    elif destination == 'api':
        load_to_api(data)
    else:
        raise ValueError("Destino de dados desconhecido.")

    return "Dados carregados com sucesso!"


def load_to_database(data):
    # Lógica de carga para um banco de dados
    print("Carregando dados no banco de dados...")


def load_to_file(data):
    # Lógica de carga para um arquivo
    print("Carregando dados em um arquivo...")


def load_to_api(data):
    # Lógica de carga para uma API
    print("Carregando dados na API...")