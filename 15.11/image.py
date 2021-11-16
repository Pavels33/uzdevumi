from PIL import Image

def bilde():

  datne = "15.11/suns_rej7-1024x724.jpg"

  with Image.open(datne) as im:
    print(datne, im.format, f"{im.size}x{im.mode}")
    im.show()
    izmers = (100,100)
    im.thumbnail(izmers)
    im.save("maza bilde.jpg", im.format)
    im.show

bilde()


im = Image.open("15.11/suns_rej7-1024x724.jpg")


angle = 90

out = im.rotate(angle)
out.save('rotate-output.png')

