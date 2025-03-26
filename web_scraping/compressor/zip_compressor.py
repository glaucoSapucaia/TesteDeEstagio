from pathlib import Path
import zipfile

class ZipCompressor:
    '''
    Zip Compressor Class
    '''
    @staticmethod
    def compress(files, zip_file_name: str, output_dir: Path):
        zip_path = output_dir / zip_file_name

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file in files:
                zip_file.write(file, file.name)
                print(f'Added file to zip - {file.name}.')
        print(f'Zip compressed in - {zip_path}')
