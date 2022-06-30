from PIL import Image
import os


def convert(fileName: str) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    im = Image.open(os.path.join(script_dir, fileName))
    width, height = im.size
    spriteLetters = ['k', 'q', 'b', 'n', 'r', 'p']
    spriteWidth = width//6
    spriteHeight = height//2
    for i in range(12):
        name = ''
        name += spriteLetters[i % 6]
        name += str(i // 6)
        name += '.png'
        imc = im.crop((
            spriteWidth * (i % 6),
            spriteHeight * (i // 6),
            spriteWidth * (i % 6 + 1),
            spriteHeight * (i // 6 + 1)
        )
        )
        imc = imc.resize((80, 80))
        imc.save(os.path.join(script_dir, name))


convert("spriteSet.png")
