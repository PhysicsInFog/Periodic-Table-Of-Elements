from PIL import Image, ImageDraw, ImageFont
from json import load
from math import floor

import warnings
warnings.filterwarnings("ignore")

width = 7680
height = 4320
path = "image.png"

side = min(width/19, height/11)
fontSmall = ImageFont.truetype("fonts/arialbd.ttf", floor(side*0.1))
fontMiddle = ImageFont.truetype("fonts/arialbd.ttf", floor(side*0.2))
fontLarge = ImageFont.truetype("fonts/arialbd.ttf", floor(side*0.35))


weight = load(open("data/weight.json"))
attribute = load(open("data/attribute.json"))
color = load(open("data/color.json"))
name = load(open("data/name.json"))
position = load(open("data/position.json"))
symbol = load(open("data/symbol.json"))

print("Creating...")
image = Image.new(
    mode="RGB",
    size=(width, height),
    color=color["background"]
)

draw = ImageDraw.Draw(image)

print("Writing...")
# Other elements
for i in range(118):
    x, y = position[i]

    draw.rectangle(
        xy=(
            width/2-side*10+side*(x+1.075),
            height/2-side*6+side*(y+1.075),
            width/2-side*10+side*(x+1.925),
            height/2-side*6+side*(y+1.925)
        ),
        outline=color[attribute[i]],
        width=floor(side*0.02)
    )

    draw.text(
        xy=(
            width/2-side*10+side*(x+1.15),
            height/2-side*6+side*(y+1.15)
        ),
        text=str(i+1),
        fill=color[attribute[i]],
        font=fontSmall
    )

    draw.text(
        xy=(
            width/2-side*10+side*(x+1.5)-fontLarge.getsize(symbol[i])[0]/2,
            height/2-side*6+side*(y+1.425)-fontLarge.getsize(symbol[i])[1]/2,
        ),
        text=symbol[i],
        fill=color[attribute[i]],
        font=fontLarge
    )

    draw.text(
        xy=(
            width/2-side*10+side*(x+1.5)-fontSmall.getsize(name[i])[0]/2,
            height/2-side*6+side*(y+1.675)-fontSmall.getsize(name[i])[1]/2,
        ),
        text=name[i],
        fill=color[attribute[i]],
        font=fontSmall
    )

    draw.text(
        xy=(
            width/2-side*10+side*(x+1.5)-fontSmall.getsize(weight[i])[0]/2,
            height/2-side*6+side*(y+1.8)-fontSmall.getsize(weight[i])[1]/2,
        ),
        text=weight[i],
        fill=color[attribute[i]],
        font=fontSmall
    )


# Lanthanide elements
draw.rectangle(
    xy=(
        width/2-side*10+side*(2+1.075),
        height/2-side*6+side*(5+1.075),
        width/2-side*10+side*(2+1.925),
        height/2-side*6+side*(5+1.925)
    ),
    outline=color["lanthanoid"],
    width=floor(side*0.02)
)

draw.text(
    xy=(
        width/2-side*10+side*(2+1.15),
        height/2-side*6+side*(5+1.15)
    ),
    text="57-71",
    fill=color["lanthanoid"],
    font=fontSmall
)

draw.text(
    xy=(
        width/2-side*10+side*(2+1.5)-fontMiddle.getsize("La-Lu")[0]/2,
        height/2-side*6+side*(5+1.45)-fontMiddle.getsize("La-Lu")[1]/2,
    ),
    text="La-Lu",
    fill=color["lanthanoid"],
    font=fontMiddle
)

draw.text(
    xy=(
        width/2-side*10+side*(2+1.5)-fontSmall.getsize("Lanthanoids")[0]/2,
        height/2-side*6+side*(5+1.7375)-fontSmall.getsize("Lanthanoids")[1]/2,
    ),
    text="Lanthanoids",
    fill=color["lanthanoid"],
    font=fontSmall
)


# Actinide elements
draw.rectangle(
    xy=(
        width/2-side*10+side*(2+1.075),
        height/2-side*6+side*(6+1.075),
        width/2-side*10+side*(2+1.925),
        height/2-side*6+side*(6+1.925)
    ),
    outline=color["actinoid"],
    width=floor(side*0.02)
)

draw.text(
    xy=(
        width/2-side*10+side*(2+1.15),
        height/2-side*6+side*(6+1.15)
    ),
    text="89-103",
    fill=color["actinoid"],
    font=fontSmall
)

draw.text(
    xy=(
        width/2-side*10+side*(2+1.5)-fontMiddle.getsize("Ac-Lr")[0]/2,
        height/2-side*6+side*(6+1.45)-fontMiddle.getsize("Ac-Lr")[1]/2,
    ),
    text="Ac-Lr",
    fill=color["actinoid"],
    font=fontMiddle
)

draw.text(
    xy=(
        width/2-side*10+side*(2+1.5)-fontSmall.getsize("Actinoids")[0]/2,
        height/2-side*6+side*(6+1.7375)-fontSmall.getsize("Actinoids")[1]/2,
    ),
    text="Actinoids",
    fill=color["actinoid"],
    font=fontSmall
)


print("Saving...")
image.save(path)

print("Saved at " + path)
