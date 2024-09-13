from PIL import Image, ImageDraw, ImageFont

# 打开原始图片
original_image = Image.open('original_image.png')

# 创建一个可以在给定图像上绘图的对象
draw = ImageDraw.Draw(original_image)

# 设置字体和大小（需要确保有相应的字体文件）
# 如果不指定字体，将使用默认字体
# font = ImageFont.truetype("arial.ttf", 45)

# 假设我们要在图片的(100, 100)位置添加文字
# 如果要替换文字，你需要先确定旧文字的位置和大小
text = "Hello, World!"
text_color = (0, 0, 0)
position = (100, 100)

# 添加文字（这里实际上是添加，如果要替换，需要覆盖旧文字的位置）
# 如果要替换，可能需要先使用某种方法（如图像处理或OCR）来确定旧文字的位置和大小
draw.text(position, text, fill=text_color, font=None)  # font=None将使用默认字体

# 保存修改后的图片
original_image.save('modified_image.png')

# 注意：这个示例只是简单地添加了文字，并没有替换图片中已有的文字。
# 要替换文字，你需要先定位旧文字，并确保新文字的大小和位置与之匹配。