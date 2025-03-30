from typing import TYPE_CHECKING
import zipfile

# Importação para tipagem
if TYPE_CHECKING:
    from pathlib import Path

class ZipCompressor:
    '''
    Classe responsável por compactar arquivos em um arquivo ZIP.
    Esta classe fornece um método estático para comprimir arquivos e armazená-los em um diretório de saída especificado.
    '''
    @staticmethod
    def compress(files: list, zip_file_name: str, output_dir: 'Path') -> None:
        '''
        Método estático para compactar uma lista de arquivos em um arquivo ZIP.

        Parâmetros:
        files (list): Lista de arquivos a serem compactados.
        zip_file_name (str): Nome do arquivo ZIP a ser criado.
        output_dir (Path): Diretório onde o arquivo ZIP será salvo.
        '''
        zip_path = output_dir / zip_file_name

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file in files:
                zip_file.write(file, file.name)

                # debug
                print(f'Added file to zip - {file.name}.')
                
        # debug
        print(f'Zip compressed in - {zip_path}')
