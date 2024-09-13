# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
import ocr_module  # 导入模块


def main():
    # 获取当前脚本所在的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取图片的绝对路径
    image_name = "example.png"  # 假设图片名为 example.png
    image_path = os.path.join(script_dir, image_name)

    # 检查图片文件是否存在
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_name}' does not exist in the current directory.")
        sys.exit(1)

    # 调用OCR函数
    recognized_text = ocr_module.ocr_image(image_path)

    # 打印识别出的文字
    print("Recognized Text:")
    print("-------------")
    print(recognized_text)

    # 尝试修改文字


if __name__ == "__main__":
    main()