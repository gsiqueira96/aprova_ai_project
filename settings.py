import os

# Configurações para a integração do CrewAI
CREWAI_API_KEY = os.getenv('CREWAI_API_KEY', 'your-default-api-key')

# Configurações de caminhos de dados
RAW_DATA_PATH = os.path.join(os.getcwd(), 'data', 'raw')
PROCESSED_DATA_PATH = os.path.join(os.getcwd(), 'data', 'processed')

# Outras configurações relevantes
LOG_LEVEL = 'DEBUG'