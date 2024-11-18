# Projeto Scraping

Para utilizar o webscrapping execute o código:

```bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
```

Para fazer a transformação dos dados e enviar para o banco de dados:
- Na pasta projeto-scraping, execute o código:

```bash
python src/transformacao/main.py 
```