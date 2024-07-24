import requests
from webscraping.parser import parse_html, parse_table


class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, endpoint):
        """
        Realiza uma requisição HTTP para obter o conteúdo da página.
        :param endpoint: URL da página a ser requisitada
        :return: Conteúdo HTML da página
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Erro ao requisitar a página: {response.status_code}")
            return None

    def scrape(self, endpoint):
        """
        Faz o scraping de uma página e analisa os dados.
        :param endpoint: URL da página a ser raspada
        :return: Dados extraídos da página
        """
        html_content = self.fetch_page(endpoint)
        if html_content:
            data = parse_html(html_content)
            return data
        else:
            return None

    def scrape_table(self, endpoint):
        """
        Faz o scraping de uma tabela em uma página e analisa os dados.
        :param endpoint: URL da página contendo a tabela
        :return: Dados extraídos da tabela
        """
        html_content = self.fetch_page(endpoint)
        if html_content:
            table_data = parse_table(html_content)
            return table_data
        else:
            return None
