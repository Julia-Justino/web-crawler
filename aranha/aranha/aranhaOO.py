import csv
import requests
import zipfile

class crawler:
    def __init__(self, url, nomeArquivo):
        self.url = url
        self.nomeArquivo = nomeArquivo
    
    def pegarDados(sefl):
        CSV_URL = sefl.url
        with requests.Session() as s:
            download = s.get(CSV_URL)
            with open(f"{sefl.nomeArquivo}"  , 'wb') as f:
                f.write(download.content)

        f = gzip.open(f"{sefl.nomeArquivo}", 'rt')
        file_content=f.read()

        cr = csv.reader(file_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row)