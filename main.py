from aprova_crew.main import initialize_agents
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from webscraping.scraper import scrape_website


def main():
    # Inicializar agentes do CrewAI
    agents = initialize_agents()

    # Executar processo de ETL
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)

    # Executar Web Scraping
    scrape_website()


if __name__ == "__main__":
    main()