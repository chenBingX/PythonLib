# coding=utf-8
from PIL import Image

IMG = "/Users/chenbing/Desktop/avart.jpg"
filePath = "/Users/chenbing/Desktop/avart.txt"
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
height = 45
width = 100


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 灰度转换公式

    unit = (256.0 + 1) / length                       # 比例
    inext = int(gray / unit)                          # 根据灰度求对应的index
    return ascii_char[inext]


if __name__ == '__main__':

    im = Image.open(IMG)                              # 读取图片
    im = im.resize((width, height), Image.NEAREST)    # 调整图片的大小

    txt = ""
    for i in range(height):                           # 遍历图片的像素点，获取每一个像素点的rgbA值
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))     # 获得相应位置像素点的值组元(a,g,b,a)
        txt += '\n'                                   # 换行

    print txt

    # 字符画输出到文件
    with open(filePath, 'w') as f:                    # 输出到指定文件
        f.write(txt)
