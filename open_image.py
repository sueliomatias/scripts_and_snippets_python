from PIL import Image

with Image.open("./assets/images/llm.jpg") as im:
    im = im.rotate(45)
    im.show()