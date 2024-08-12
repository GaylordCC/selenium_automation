from bs4 import BeautifulSoup
import copy
import pandas as pd
from main_draft import current_url


browser = current_url()

class Bs4:
    def __init__(self) -> None:
        pass

    def bs4_method(self, browser):
        html=browser.page_source
        soup=BeautifulSoup(html,'html.parser')
        div = soup.find_all("div", "jsx-4130407500 table-stats-container")
        cols = div[0].find_all("tr", {'class':"Table__sub-header Table__TR Table__even"})[0].find_all("th", {"class": "Table__TH"})
        cols = [col.text for col in cols]
        vals = div[0].find_all("tr", "Table__TR Table__TR--sm Table__odd")[0].find_all("td")
        vals = [val.text for val in vals]
        print("Number of Records:", len(div[0].find_all("tr", "Table__TR Table__TR--sm Table__odd")))
        data = []
        for i in range(0, len(div[0].find_all("tr", "Table__TR Table__TR--sm Table__odd"))):
            vals = div[0].find_all("tr", "Table__TR Table__TR--sm Table__odd")[i].find_all("td")
            vals = [val.text for val in vals]
            row = {}
            for j in range(0,len(vals)):
                row[cols[j]] = vals[j]
            data.append(copy.deepcopy(row))
        projections = pd.DataFrame(data)

        return projections