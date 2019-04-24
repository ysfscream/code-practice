from PIL import Image, ImageFont, ImageDraw

"""
在图片上加入文字
"""

image = Image.open('1.jpeg')
width, height = image.size

print('size is w: {0}, h: {1}'.format(width, height))

# 缩放到50%
image.thumbnail((width//2, height//2))

# 加载字体
font = ImageFont.truetype('Arial.ttf', 56)

draw = ImageDraw.Draw(image)
draw.text((width / 5, height / 5), 'Your Name', fill=(0, 0, 0), font=font)

image.save('2.jpg', 'jpeg')
