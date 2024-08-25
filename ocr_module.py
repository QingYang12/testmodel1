# ocr_module.py

from PIL import Image
import pytesseract


def ocr_image(image_path):
    # 加载图片到PIL图像对象
    image = Image.open(image_path)

    # 使用pytesseract执行OCR
    text = pytesseract.image_to_string(image)

    # 返回识别出的文字
    return text.strip()