from requests import get
from bs4 import BeautifulSoup
import csv

def getElement(soup, balise, classe):
    liste = soup.find_all(balise, class_=classe)
    to_return = []
    for element in liste:
        to_return.append(element.string)
    return to_return

url = 'https://www.gov.uk/search/news-and-communications'

page = get(url)

soup = BeautifulSoup(page.content, 'html.parser')



liste_titres = getElement(soup, 'a', 'gem-c-document-list__item-title')




liste_desc=getElement(soup, 'p', "gem-c-document-list__item-description")




en_tete=["titre", "description"]

with open('data.csv', "w") as csv_file:
    writer= csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)

    for title, desc in zip(liste_titres, liste_desc):
        ligne= [title.string, desc.string]
        writer.writerow(ligne)