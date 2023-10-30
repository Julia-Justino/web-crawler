import aranhaOO

crawler = aranhaOO.crawler(
    url='https://archive.ics.uci.edu/static/public/468/online+shoppers+purchasing+intention+dataset.zip',
    nomeArquivo='online+shoppers+purchasing+intention+dataset.zip'
)

crawler.pegarDados()