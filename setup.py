from setuptools import setup, find_packages

setup(
    name="aprova_ai_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'crewai',
        'crewai-tools',
        'requests',
        'beautifulsoup4',
        'selenium',
        'pandas',
        'numpy',
        'jupyter'
    ],
    entry_points={
        'console_scripts': [
            'aprova_ai=main:main',
        ],
    },
    author="Seu Nome",
    author_email="seuemail@dominio.com",
    description="Projeto para Aprova AI utilizando CrewAI, ETL, e Web Scraping",
    license="MIT",
    keywords="crewAI etl webscraping ai",
    url="http://projeto-aprova-ai.com",   # URL do projeto
    project_urls={
        "Bug Tracker": "http://projeto-aprova-ai.com/issues",
    },
)