from bs4 import BeautifulSoup


def parse_html(html_content):
    """
    Analisa o conteúdo HTML e extrai dados relevantes.
    :param html_content: String contendo o HTML
    :return: Dicionário com os dados extraídos
    """
    soup = BeautifulSoup(html_content, "html.parser")
    parsed_data = {
        "title": soup.title.string if soup.title else "No Title",
        "headings": [heading.get_text() for heading in soup.find_all("h1")],
        # Adicione mais extrações conforme necessário
    }
    return parsed_data


def parse_table(html_content):
    """
    Analisa uma tabela HTML e converte para uma lista de dicionários.
    :param html_content: String contendo o HTML
    :return: Lista de dicionários com os dados da tabela
    """
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")
    headers = [header.get_text() for header in table.find_all("th")]
    rows = table.find_all("tr")

    table_data = []
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == len(headers):
            table_data.append(
                {headers[i]: cells[i].get_text() for i in range(len(headers))}
            )

    return table_data
