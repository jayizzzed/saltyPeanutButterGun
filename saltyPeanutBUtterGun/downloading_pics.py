import requests
from PIL import Image
from io import BytesIO


url = "http://acervo.estadao.com.br/publicados/1973/03/22/m/19730322-30054-nac-0114-999-116-not.jpg"

r = requests.get(url)

in_bytes = r.content

i = Image.open(BytesIO(in_bytes))

x = 0

suffix = ".jpg"

categorie = "reddit_meme"

while x < 5:
    filename = categorie + " " + str(x) + suffix
    i.save("pics/{}".format(filename))
    x = x+1
