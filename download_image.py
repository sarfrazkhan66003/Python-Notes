from urllib .request import urlretrieve
from PIL import Image

print("Image downloading start")
imageUrl = "https://www.hindustantimes.com/static-content/1y/cricket-logos/players/virat-kohli.png"
urlretrieve(imageUrl,"image.png")

image = Image.open("./image.png")
image.show()