
# PDF Table Extractor e Compressor

Este projeto tem como objetivo **extrair tabelas** de um arquivo PDF e **salvar as informações em formato CSV**. Além disso, o arquivo CSV gerado é **compactado em um arquivo ZIP**. O script utiliza classes modulares para extrair os dados do PDF, processá-los e salvar no formato desejado.

## Funcionalidades

1. **Extração de Tabelas do PDF**: A classe `TableExtractor` usa o `PdfExtractor` para ler as páginas do PDF e extrair as tabelas.
2. **Processamento de Dados**: O `DataProcessor` processa os dados extraídos, aplicando alterações definidas no dicionário de `abbreviation_dict`.
3. **Salvamento em CSV**: Os dados processados são salvos em formato CSV usando o `CsvSaver`.
4. **Compactação de Arquivos**: O arquivo CSV gerado é compactado em um arquivo ZIP com a ajuda do `ZipCompressor`.

## Dependências

Este projeto depende de algumas bibliotecas para processamento e manipulação de dados. As bibliotecas necessárias são:

- `pandas` — Para manipulação de dados em formato tabular.
- `tabula-py` — Para extração de conteúdo do PDF.
- `zipfile` — Para compactação do arquivo CSV.
- `openjdk 11` — Para o uso de tabula-py.

Verifique se o openjdk 11 está instalado:

```bash
java --version
```

Caso não esteja instalado, ou exita outra versão no sistema, use:

Para instalação:

```bash
sudo apt install openjdk-11-jdk
```

Para selecionar a versão 11:

```bash
sudo update-alternatives --config java

Existem 2 escolhas para a alternativa java (disponibiliza /usr/bin/java).

  Selecção   Caminho                                      Prioridade Estado
------------------------------------------------------------
  0            /usr/lib/jvm/java-17-openjdk-amd64/bin/java   1711      modo automático
* 1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java   1111      modo manual
  2            /usr/lib/jvm/java-17-openjdk-amd64/bin/java   1711      modo manual

Pressione <enter> para manter a escolha actual[*], ou digite o número da selecção:
```

Instale as dependências com:

```bash
pip install pandas tabula-py
```

## Como Usar

1. **Clone o repositório** ou faça o download do código.
2. **Crie os diretórios necessários**: O script usa o diretório `csv/` para armazenar o arquivo CSV gerado. O arquivo PDF de entrada deve ser colocado no diretório `pdf/`.
3. **Execute o script** `main.py`:

```bash
python3 main.py
```

### Personalização

- **Caminho do PDF**: A variável `PDF_PATH` está configurada para um PDF específico, mas você pode alterar o caminho do arquivo PDF no código para outro PDF de sua escolha.
- **Dicionário de Abreviações**: O dicionário `abbreviations_dict` permite que você defina nomenclaturas a serem usadas no processamento de dados, neste caso, nome de colunas.

## Estrutura do Projeto

```
.
├── csv/                                   
│   ├── Teste_glauco_sapucaia/             # Pasta de extração arquivo ZIP
│   │   └── Anexo_I                        # Arquivo CSV descompactado
│   ├── Anexo_I                            # Arquivo CSV gerado e alterado
│   └── Teste_glauco_sapucaia.zip          # Arqvuio CSV compactado
├── pdf/                                   
│   └── Anexo_I                            # PDF de entrada
├── src/                                   
│   ├── __init__.py                        
│   ├── base.py                            # Interfaces
│   ├── csv_saver.py                       # Salva o arqvuio CVS
│   ├── data_processor.py                  # Processa os dados da tabela
│   ├── pdf_extractor.py                   # Extrai as tabelas do arquivo PDF 
│   ├── table_extractor.py                 # Classe principal gerenciadora
│   └── zip_compressor.py                  # Compacta o arquivo em ZIP
├── main.py                                # Script principal
└── README.md                              # Este arquivo
```

## Exemplo de Saída

Ao executar o script, você verá algo como:

```
Tabela extraída com sucesso - Total de linhas da página um: 150.
Arquivo CSV criado - csv/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv
Tabela salva e compactada em csv/Teste_glauco_sapucaia.zip
```

A tabela extraída será salva como `Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv` no diretório `csv/`, e o arquivo será compactado como `Teste_glauco_sapucaia.zip`.

## Contribuições

Se você deseja contribuir com o projeto, sinta-se à vontade para abrir um **pull request** ou **issue**.
