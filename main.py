'''
Aqui nós temos o arquivo principal para rodar o webscraping no site do 
Skyscanner (https://www.skyscanner.com.br/) para a captação de passagens aéreas de acordo com o destino,
local de saída, a data de ida e a de volta. ----

Here we have the main file to run the webscraping on the site
Skyscanner (https://www.skyscanner.com.br/) for capturing airline tickets according to destination,
departure location, departure date and return date. ----

Qui abbiamo il file principale per eseguire il webscraping sul sito
Skyscanner (https://www.skyscanner.com.br/) per acquisire i biglietti aerei in base alla destinazione,
luogo di partenza, data di partenza e data di ritorno. ---
'''
# %% importando os patotes / importing the packages / importazione dei pacchetti
import pandas as pd
import requests
from bs4 import BeautifulSoup
from generation_links import gerando_link


# %% Capturando links

'''
Aqui deve-se seguir o padrão : de onde sai, para onde vai, data de partida e data de chegada. 
Obs.: A data deve ser colocada no padrão USA (YMD). Caso não tenha data de chegada, coloca '' vazio. ----

Here you must follow the pattern: where you leave, where you are going, date of departure and date of arrival.
Note: The date must be placed in the USA standard (YMD). If you don't have an arrival date, put '' empty. ----

Qui devi seguire lo schema: dove parti, dove vai, data di partenza e data di arrivo.
Nota: la data deve essere inserita nello standard USA (YMD). Se non hai una data di arrivo, metti '' vuoto. ----
'''

gerando_link('bsb', 'rome','240201','')  