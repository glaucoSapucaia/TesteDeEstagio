
# PDF Downloader e Compressor

Este script realiza o **download de arquivos PDF** a partir de uma URL e os **compacta** em um arquivo ZIP. Ele utiliza a classe `TestPDFDownloader` para fazer o download dos PDFs e a classe `ZipCompressor` para compactá-los.

## Funcionalidades

1. **Download de PDFs**: Baixa arquivos PDF de uma URL específica.
2. **Filtragem de PDFs**: Baixa apenas PDFs com nomes específicos (começando com "Anexo_I" ou "ANEXO_II").
3. **Compactação de PDFs**: Após o download, os arquivos são compactados em um arquivo ZIP.

## Dependências

- `requests` — Para fazer as requisições HTTP e baixar os arquivos.
- `beautifulsoup4` — Para fazer o parsing do HTML e extrair os links para os PDFs.
- `pathlib` — Para manipulação de caminhos de arquivos.
- `zipfile` — Para compactação dos arquivos em formato ZIP.

Instale as dependências com:

```bash
pip install requests beautifulsoup4
```

## Como Usar

1. **Clone o repositório** ou faça o download do código.
2. **Execute o script**:

```bash
python3 main.py
```

### Personalização

- O script está configurado para baixar PDFs da URL:  
  `https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos`.  
  Caso queira usar outra URL, basta modificar a variável `url` no código.

- O diretório de saída para os PDFs baixados está configurado para ser o diretório `pdfs` na raiz do projeto. Diretório definido pela constante `PATH_DIR`.

## Estrutura do Projeto

```
.
├── compressor/          
│   ├── __init__.py                
│   └── zip_compressor.py          # Compactação dos arquivos em ZIP
├── downloader/                
│   ├── __init__.py                
│   ├── base.py                    # Interface de TestPDFDownloader
│   └── test_downloader.py         # Download de PDFs
├── pdfs/
│   ├── Anexo_II                   # Arquivo PDF
│   ├── Anexo_I                    # Arquivo PDF
│   └── pdfs_files.zip             # Arquivos PDF compactados
├── main.py                        # Script principal
└── README.md                      # Este arquivo
```

## Exemplo de Saída

Ao executar o script, você verá algo como:

```
PDF Downloaded - Anexo_I.pdf.
PDF Downloaded - ANEXO_II.pdf.
Tudo certo! PDFs baixados e compactados...
```

Os arquivos PDF serão baixados para o diretório `pdfs/` e compactados em `pdfs_files.zip`.

## Contribuições

Se você deseja contribuir com o projeto, sinta-se à vontade para abrir um **pull request** ou **issue**.
