from PIL import Image, ImageDraw, ImageFont

# 加载原始图像
original_image = Image.open('original_image1.png')

# 尝试加载字体，如果默认字体不可用，则加载一个具体的字体文件
try:
    font = ImageFont.load_default()
except IOError:
    font = ImageFont.truetype("path/to/your/font.ttf", size=20)

# 新文本
new_text = "Jello, World!"
text_color = (0, 0, 0)  # 文本颜色
background_color = (255, 255, 255)  # 假设背景色是白色
# 原有文本的位置（这些值需要您根据实际情况来确定）
x_old, y_old = 100, 100  # 假设这是您想要覆盖的文本的位置



# 创建一个可以在给定图像上绘图的对象
draw = ImageDraw.Draw(original_image)

# 使用背景色绘制一个矩形来覆盖原有文本（假设新文本足够大或位置正确）
text_bbox = draw.textbbox((0, 0), new_text, font=font)
left, upper, right, lower = text_bbox
# 计算文本的宽度和高度
text_width = right - left
text_height = lower - upper
print(f"Text Width: {text_width}, Text Height: {text_height}")
#draw.rectangle([(x_old, y_old), (x_old + 16, y_old + 16)], fill=background_color)
# 如果您想将边界框绘制到图像上（可选）
draw.rectangle([(x_old, y_old), (x_old + text_width, y_old + text_height)], fill=background_color)


# 在同一位置绘制新文本
draw.text((x_old, y_old), new_text, fill=text_color, font=font)
# 保存或显示修改后的图像
original_image.save('modified_image1.png')
# 或者使用 original_image.show() 来直接显示图像（这取决于您的环境）