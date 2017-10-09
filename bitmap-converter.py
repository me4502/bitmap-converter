import math
from PIL import Image


def txt_to_png(filename):
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip().replace(",", "").replace("0b", "").replace(" ", "") for x in content]
        print(content)
        im = Image.new("RGB", (len(content[0]), len(content)))
        pix = im.load()
        for y in range(len(content)):
            line = content[y]
            for x in range(len(line)):
                pix[x, y] = (0, 0, 0) if line[x] == '1' else (255, 255, 255)
        im.save(filename + ".png", "PNG")


def png_to_txt(filename):
    im = Image.open(filename).convert('RGB')
    pix = im.load()
    width, height = im.size
    content = []
    for y in range(height):
        line = "    "
        for chunk in range(int(math.ceil(width / 8.0))):
            line += "0b"
            for x in range(8):
                if chunk * 8 + x >= width:
                    line += '0'
                else:
                    line += '0' if (pix[chunk * 8 + x, y][0] > 127) else '1'
            line += ", "
        content.append(line)
    with open(filename + '.txt', 'w+') as f:
        for item in content:
            f.write("%s\n" % item)


if __name__ == "__main__":
    txt_to_png("testcase.txt")
    png_to_txt("testcase.txt.png")
