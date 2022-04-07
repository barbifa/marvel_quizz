from components import vars
from PIL import Image

def total(value):
    # do some logic to see which character you selected

    if value >=999 :
        print("=) All of them are awesome! So, no heroes for you today hahaha")
    elif value == 10:
        print("It's " + vars.characters[0])
        im = Image.open("img/bw.jpg")
        im.show()
    elif value == 14:
        print("It's " + vars.characters[1])
        im = Image.open("img/g.png")
        im.show()
    elif value == 16:
        print("It's " + vars.characters[2])
        im = Image.open("img/cm.jpg")
        im.show()
    elif value == 18:
        print("It's " + vars.characters[3])
        im = Image.open("img/scar.jpg")
        im.show()
    else:
        print("Sorry, I count not guess what character you were thinking about =( ")
        # add some emoji icons, or show the character image using the Pillow package
