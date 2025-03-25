from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests
import zipfile

ROOT_DIR = Path(__file__).parent.resolve()
PATH_DIR = ROOT_DIR / 'pdfs'
PATH_DIR.mkdir(exist_ok=True)

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

# print(ROOT_DIR)

def pdf_downloader(url_page, folder_dir):
    answer = requests.get(url_page)

    if answer.status_code == 200:
        soup = BeautifulSoup(answer.content, 'html.parser')

        pdf_links = soup.find_all('a', href=True)
        pdfs = []

        for link in pdf_links:
            href = link['href']

            if href.endswith('.pdf'):
                pdf_url = urljoin(url_page, href)
                pdf_name = Path(urlparse(pdf_url).path).name

                if pdf_name.startswith(('Anexo_I', 'ANEXO_II')):
                    pdf_file = folder_dir / pdf_name
                    pdf_answer = requests.get(pdf_url)

                    if pdf_answer.status_code == 200:
                        with open(pdf_file, 'wb') as file:
                            file.write(pdf_answer.content)
                        
                        pdfs.append(pdf_file)
                        print(f'PDF Downloaded - {pdf_name}.')
        
        return pdfs
    else:
        print('Something went wrong!')

def zip_compress(files, zip_file_name, zipe_file_dir):
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file in files:
            zip_file.write(file, file.name)
            print(f'Add file to zip - {file.name}.')
    print(f'Zip compressed in {zipe_file_dir}.')

if __name__ == '__main__':
    dowloaded_pdfs = pdf_downloader(url, PATH_DIR)
    zip_compress(dowloaded_pdfs, 'pdfs_files.zip', PATH_DIR)