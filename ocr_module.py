# ocr_module.py

from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # 修改为你的实际路径

def ocr_image(image_path):
    # 加载图片到PIL图像对象
    image = Image.open(image_path)

    # 使用pytesseract执行OCR
    text = pytesseract.image_to_string(image, lang='chi_sim')

    # 返回识别出的文字
    return text.strip()

def ocr_image2(image_path):
    # 加载图片到 OpenCV 图像对象
    image = cv2.imread(image_path)

    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用 Tesseract OCR 引擎执行 OCR
    #切换识别中文还是英文
    text = pytesseract.image_to_string(gray, lang='chi_sim')

    # 返回识别出的文字
    return text.strip()