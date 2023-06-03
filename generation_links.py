'''
Aqui será gerado e coletado os links do scraping.---
Here the scraping links will be generated and collected.---
Qui verranno generati e raccolti i link di scraping.---
'''


# %% importando os patotes / importing the packages / importazione dei pacchetti
import requests
import pandas as pd
from bs4 import BeautifulSoup

# %% Gerando os links / / 
 
def gerando_link(de,para,ida,volta):
    if volta=='':
        url=f'https://www.skyscanner.com.br/transporte/passagens-aereas/{de}/{para}/{ida}'
    else:
        url=f'https://www.skyscanner.com.br/transporte/passagens-aereas/{de}/{para}/{ida}/{volta}'
    return print(url)

